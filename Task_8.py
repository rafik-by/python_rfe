from random import *


target = randint(1,100)

while True:
    b = int(input("Введите число: ")) 
    if  b == target :
        print("Число найдено")
        break
    elif b > target: 
        print("Число больше")
    else:
        print("Число меньше")