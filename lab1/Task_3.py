money = int(input("Введите сумма, которую хотите конвертнуть"))

l100 = money // 100
money %= 100
l50 = money//50
money %= 50
l10 = money // 10 
money %= 10
l5 = money //5
money %= 5
l2 = money // 2 
money %= 2
l1 = money // 1
money %= 1 



print(f"купюр по 100:{l100}",
      f"купюр по 50:{l50}",
      f"купюр по 10:{l10}",
      f"купюр по 5:{l5}",
      f"купюр по 2:{l2}",
      f"купюр по 1:{l1}",
      sep = '\n')

