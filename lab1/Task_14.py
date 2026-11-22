list1 = [float(x) for x in input("Введите первый набор чисел через пробел: ").split()]
list2 = [float(x) for x in input("Введите второй набор чисел через пробел: ").split()]

set1 = set(list1)
set2 = set(list2)


common = set1 & set2

only_in_first = set1 - set2
only_in_second = set2 - set1


symmetric_diff = set1 ^ set2


print(f"1. Числа в обоих наборах одновременно: {sorted(list(common))}",
        f"2. Только в первом наборе: {sorted(list(only_in_first))}",
        f"   Только во втором наборе: {sorted(list(only_in_second))}",
        f"3. Числа за исключением общих: {sorted(list(symmetric_diff))}",
        sep = "\n")