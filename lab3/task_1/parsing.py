import json
import re
import time
from collections import Counter
from dataclasses import asdict, dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://24afisha.by"
KINO_URL = "https://24afisha.by/ru/minsk/events/kino"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    )
}


@dataclass
class KinoEvent:
    title: str
    date_time: str
    venue: str
    price: float | None
    age_limit: str
    url: str


def extract_price(text: str) -> float | None:
    """Достаёт число из строки вида 'от 8.00 Б' или '12,50 BYN'."""
    cleaned = text.replace("\xa0", " ")
    match = re.search(r"от\s*(\d+(?:[.,]\d+)?)", cleaned, re.IGNORECASE)
    if not match:
        match = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:Б|BYN|руб)", cleaned, re.IGNORECASE)
    return float(match.group(1).replace(",", ".")) if match else None


def extract_age(text: str) -> str:
    """Достаёт возрастное ограничение вида '12+', '16+', '18+'."""
    match = re.search(r"\b(?:0|6|12|16|18)\+", text)
    return match.group(0) if match else "0+"


def parse_event_details(session: requests.Session, event_url: str) -> tuple[str, str, float | None, str]:
    """
    Заходит на страницу конкретного фильма и забирает:
    площадку (кинотеатр), время сеанса, цену (если не нашлась в карточке) и возраст.
    """
    venue = "Не указано"
    show_time = ""
    price = None
    age = "0+"

    try:
        resp = session.get(event_url, timeout=10)
        if not resp.ok:
            return venue, show_time, price, age

        soup = BeautifulSoup(resp.text, "lxml")
        page_text = soup.get_text(" ", strip=True)

        place_link = soup.select_one(
            'a[href*="/places/"], a[href*="/place/"], a[href*="/cinemas/"], a[href*="/cinema/"]'
        )
        if place_link:
            venue = place_link.get_text(strip=True)

        time_match = re.search(r"\b([01]?\d|2[0-3]):[0-5]\d\b", page_text)
        if time_match:
            show_time = time_match.group(0)

        price = extract_price(page_text)
        age = extract_age(page_text)

    except requests.RequestException:
        pass

    return venue, show_time, price, age


def parse_kino_afisha(limit: int | None = None) -> list[KinoEvent]:
    """Парсит раздел 'Кино' на 24afisha.by."""
    session = requests.Session()
    session.headers.update(HEADERS)

    resp = session.get(KINO_URL, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    events: list[KinoEvent] = []
    seen_urls: set[str] = set()

    
    links = soup.select('a[href*="/ru/minsk/event/"]')

   
    unique_cards = []
    for link in links:
        href = link.get("href", "").split("?")[0]
        full_url = urljoin(BASE_URL, href)
        if full_url in seen_urls:
            continue
        seen_urls.add(full_url)
        unique_cards.append((full_url, link))

    if limit:
        unique_cards = unique_cards[:limit]

    print(f"Найдено уникальных фильмов: {len(unique_cards)}. Начинаю сбор данных...")

    for idx, (full_url, link) in enumerate(unique_cards, start=1):
        
        card = link.parent if link.parent else link
        card_text = card.get_text(" ", strip=True)


        title_tag = card.find(["h2", "h3", "h4"]) or link
        title = title_tag.get_text(" ", strip=True)
       
        if not title or len(title) < 2:
            title = full_url.rstrip("/").split("/")[-1]

        price = extract_price(card_text)
        age_limit = extract_age(card_text)

        date_match = re.search(
            r"(?:с\s+)?\d{1,2}\s+(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)",
            card_text,
            re.IGNORECASE,
        )
        date_str = date_match.group(0) if date_match else "Сегодня"

       
        venue, show_time, detail_price, detail_age = parse_event_details(session, full_url)
        if price is None:
            price = detail_price
        if age_limit == "0+" and detail_age != "0+":
            age_limit = detail_age

        date_time = f"{date_str}, {show_time}" if show_time else date_str

        events.append(
            KinoEvent(
                title=title,
                date_time=date_time,
                venue=venue,
                price=price,
                age_limit=age_limit,
                url=full_url,
            )
        )

        print(f"[{idx}/{len(unique_cards)}] {title} | {price} BYN | {venue}")
        time.sleep(0.3)

    return events


def save_report(events: list[KinoEvent], txt_path: str = "kino_report.txt", json_path: str = "kino_events.json") -> None:
    """Считает аналитику, выводит в консоль и сохраняет результаты в TXT и JSON."""
    if not events:
        print("Мероприятия не найдены.")
        return

    priced = [e for e in events if e.price is not None]
    venues = [e.venue for e in events if e.venue != "Не указано"]

    lines = [
        "\n" + "=" * 50,
        f"Раздел: Кино ({KINO_URL})",
        f"Всего собрано мероприятий: {len(events)}",
        "-" * 50,
    ]

    if priced:
        min_event = min(priced, key=lambda e: e.price)
        max_event = max(priced, key=lambda e: e.price)
        avg_price = sum(e.price for e in priced) / len(priced)

        lines.extend([
            f"Минимальная стоимость билета: {min_event.price:.2f} BYN",
            f"Максимальная стоимость билета: {max_event.price:.2f} BYN",
            f"Средняя стоимость билета: {avg_price:.2f} BYN",
            f"Самое дешёвое мероприятие: {min_event.title} ({min_event.price:.2f} BYN)",
            f"Самое дорогое мероприятие: {max_event.title} ({max_event.price:.2f} BYN)",
        ])
    else:
        lines.append("Цены на билеты не удалось определить.")

    if venues:
        busiest_venue, count = Counter(venues).most_common(1)[0]
        lines.append(f"Самая загруженная площадка: {busiest_venue} ({count} мероприятий)")
    else:
        lines.append("Самая загруженная площадка: не определена")

    lines.append("-" * 50)
    lines.append("Список мероприятий:")
    for i, e in enumerate(events, start=1):
        price_str = f"{e.price:.2f} BYN" if e.price is not None else "Нет цены"
        lines.append(f"{i}. {e.title} | {e.date_time} | {e.venue} | {price_str} | {e.age_limit}")

    report_text = "\n".join(lines)
    print(report_text)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(report_text + "\n")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in events], f, ensure_ascii=False, indent=2)

    print(f"\nРезультаты сохранены в {txt_path} и {json_path}")


if __name__ == "__main__":
    kino_events = parse_kino_afisha(limit=None)
    save_report(kino_events)