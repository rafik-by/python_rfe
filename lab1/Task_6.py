list = input("Введите месяц(цифрой) через пробел число месяца: ").split()

print("Ваша дата рождения: ", "0" + list[1] if int(list[1])< 10 else list[1],
      ".","0" + list[0] if int(list[0])< 10 else list[0], sep="")
print('Ваш знак зодиака: ', end = "")
match list[0]:
    case '1':
        if int(list[1])<= 20:
            print("козерог")
        else:
            print("Водолей") 
    case '2':
        if int(list[1])<= 18:
            print("Водолей")
        else:
            print("Рыбы")
    case '3':
        if (int(list[1])<= 20):
            print("Рыбы")
        else:
            print("Овен")
    case '4':
        if int(list[1])<= 19:
            print("Овен")
        else:
            print("Телец")
    case '5':
        if int(list[1])<= 20:
            print("Телец")
        else:
            print("Близнецы")
    case '6':
        if int(list[1])<= 20:
            print("Близнецы")
        else:
            print("Рак")
    case '7':
        if int(list[1]) <= 22:
            print("Рак")
        else:
            print("Лев")
    case '8':
        if int(list[1])<= 22:
            print("Лев")
        else:
            print("Дева")
    case '9':
        if int(list[1])<= 22:
            print("Дева")
        else:
            print("Весы")
    case '10':
        if int(list[1])<= 21:
            print("Весы")
        else:
            print("Скорпион")
    case '11':
        if int(list[1])<= 21:
            print("Скорпион")
        else:
            print("Стрелец")
    case '12':
        if int(list[1])<= 21:
            print("Стрелец")
        else:
            print("Козерог")  