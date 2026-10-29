raw_input = input("Введите числа через пробел: ").split()
numbers = [float(x) for x in raw_input]

if not numbers:
    print("Список пуст.")
else:
    unique_numbers = [x for x in numbers if numbers.count(x) == 1]
    repeated_numbers = list(set([x for x in numbers if numbers.count(x) > 1]))
    even_numbers = [x for x in numbers if x.is_integer() and int(x) % 2 == 0]
    odd_numbers = [x for x in numbers if x.is_integer() and int(x) % 2 != 0]
    negative_numbers = [x for x in numbers if x < 0]
    floats = [x for x in numbers if not x.is_integer()]
    sum_divisible_by_5 = sum(x for x in numbers if x.is_integer() and int(x) % 5 == 0)

    max_num = max(numbers)
    min_num = min(numbers)

    print(f"1. Уникальные числа: {unique_numbers}",
            f"2. Повторяющиеся числа: {repeated_numbers}",
            f"3. Четные числа: {even_numbers}, Нечетные числа: {odd_numbers}",
            f"4. Отрицательные числа: {negative_numbers}",
            f"5. Дробные числа: {floats}",
            f"6. Сумма чисел, кратных 5: {sum_divisible_by_5}",
            f"7. Самое большое число: {max_num}",
            f"8. Самое маленькое число: {min_num}",
            sep = "\n")