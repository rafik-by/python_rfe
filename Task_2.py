code = input("Введите ваш пароль: ")
if len(code) < 16:
    print("Слишком короткий пароль")
elif code.isdigit() or code.isalpha():
    print('Слабый пароль')
else:
    print("Надежный пароль")