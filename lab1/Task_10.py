# Ввод данных
amount = float(input("Введите сумму покупки (руб.): "))
age = int(input("Введите возраст покупателя: "))
is_birthday = input("Сегодня день рождения? (да/нет): ").strip().lower() == "да"
is_vip = input("Покупатель имеет статус VIP? (да/нет): ").strip().lower() == "да"


base_discount = 10 if amount > 1000 else 0


if is_vip:
    current_discount = max(base_discount, 15)
else:
    current_discount = base_discount


if age >= 63:
    current_discount += 5

if is_birthday:
    current_discount += 5


total_discount = min(current_discount, 25)


discount_amount = amount * (total_discount / 100)
final_price = amount - discount_amount



print(f"Итоговая скидка: {total_discount}%",
      f"Сумма скидки: {discount_amount:.2f} руб.", 
      f"Сумма к оплате: {final_price:.2f} руб.",
      sep = '\n')