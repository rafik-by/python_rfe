
age = int(input("Возраст (лет): "))
income = float(input("Ежемесячный доход (руб.): "))
loan = float(input("Сумма кредита (руб.): "))
months = int(input("Срок кредита (мес.): "))
history = input("Кредитная история (отличная/хорошая/удовлетворительная/плохая): ").lower().strip()
has_guarantor = input("Есть поручитель? (да/нет): ").lower().strip() == "да"
has_collateral = input("Есть залог? (да/нет): ").lower().strip() == "да"


monthly_pay = loan / months
ratio = (monthly_pay / income) * 100

# 3. Подсчет баллов
score = 0

# Баллы за кредитную историю
if history == "отличная":
    score += 40
elif history == "хорошая":
    score += 30
elif history == "удовлетворительная":
    score += 15

# Баллы за нагрузку на доход
if ratio <= 30:
    score += 30
elif ratio <= 50:
    score += 15

# Баллы за возраст
if 21 <= age <= 60:
    score += 20
elif age >= 18:
    score += 10

# Баллы за залог и поручителя
if has_collateral:
    score += 10
if has_guarantor:
    score += 10

# 4. Определение категории риска и рекомендации
if age < 18 or history == "плохая" or ratio > 80:
    risk = "критический"
    rate = "—"
    decision = "Отклонить (слишком высокий риск или стоп-факторы)"
elif score >= 70:
    risk = "низкий"
    rate = "13%"
    decision = "Одобрить кредит"
elif score >= 50:
    risk = "средний"
    rate = "18%"
    decision = "Одобрить кредит"
else:
    risk = "высокий"
    rate = "24%"
    decision = "Одобрить только под залог или уменьшить сумму"

# 5. Вывод
print("\n--- Результаты ---")
print(f"Ежемесячный платеж: {monthly_pay:.2f} руб.")
print(f"Нагрузка на доход: {ratio:.1f}%")
print(f"Категория риска: {risk}")
print(f"Ставка: {rate}")
print(f"Решение: {decision}")