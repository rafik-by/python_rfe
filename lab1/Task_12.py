text = input("Введите текст: ").lower()


for punct in [".", ",", "!", "?", ":", ";", "-", "(", ")", '"']:
    text = text.replace(punct, " ")


words = text.split()


print("Всего слов:", len(words))


counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
print("Частота слов:", counts)


most_common = max(counts, key=counts.get)
print(f"Самое частое слово: '{most_common}' ({counts[most_common]} раз)")


shortest = min(words, key=len)
longest = max(words, key=len)
print(f"Самое короткое слово: '{shortest}' (букв: {len(shortest)})")
print(f"Самое длинное слово: '{longest}' (букв: {len(longest)})")




filtered_words = []
for w in words:
    if len(w) >= 3:
        filtered_words.append(w)

print("\n Анализ слов длиной от 3 символов")
if not filtered_words:
    print("Подходящих слов нет.")
else:
    print("Всего слов:", len(filtered_words))

    counts_filtered = {}
    for w in filtered_words:
        if w in counts_filtered:
            counts_filtered[w] += 1
        else:
            counts_filtered[w] = 1
    print("Частота слов:", counts_filtered)

    most_common_filtered = max(counts_filtered, key=counts_filtered.get)
    print(f"Самое частое слово: '{most_common_filtered}' ({counts_filtered[most_common_filtered]} раз)")


    shortest_filtered = min(filtered_words, key=len)
    longest_filtered = max(filtered_words, key=len)
    print(f"Самое короткое слово: '{shortest_filtered}' (букв: {len(shortest_filtered)})")
    print(f"Самое длинное слово: '{longest_filtered}' (букв: {len(longest_filtered)})")