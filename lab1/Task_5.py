list = input("Введите через пробел два числа: ").split()
for i in range(len(list)):
    list[i] = int(list[i])

flag = False

if list[1] == 0:
    flag = True
print(f"Сумма a+b: {list[0]+list[1]}", f"Разность a-b: {list[0]-list[1]}",
       f"произведение a*b: {list[0]*list[1]}","Деление на ноль.... " if flag else f"частное a//b: {list[0]//list[1]}",
         "Нельзя найти остаток деление на ноль...." if flag else f"остаток a%b: {list[0]%list[1]}", f"степень a**b: {list[0]**list[1]}", sep = "\n")