key = input("Введите ключ (1-масса, 2-длина, 3-время): ").strip()

base_from = 0.0
base_to = 0.0

match key:
    case '1':
        print("Доступные единицы: г, кг, т")
        units = input("Введите исходную и целевую единицу через пробел (например, кг г): ").split()
        val = float(input("Введите значение: "))
        
        from_u, to_u = units[0], units[1]
        
        match from_u:
            case 'г':  base_from = 0.001
            case 'кг': base_from = 1.0
            case 'т':  base_from = 1000.0

        match to_u:
            case 'г':  base_to = 0.001
            case 'кг': base_to = 1.0
            case 'т':  base_to = 1000.0

    case '2':
        print("Доступные единицы: мм, см, м, км")
        units = input("Введите исходную и целевую единицу через пробел (например, км м): ").split()
        val = float(input("Введите значение: "))
        
        from_u, to_u = units[0], units[1]
        
        # Базовая единица — метр
        match from_u:
            case 'мм': base_from = 0.001
            case 'см': base_from = 0.01
            case 'м':  base_from = 1.0
            case 'км': base_from = 1000.0

        match to_u:
            case 'мм': base_to = 0.001
            case 'см': base_to = 0.01
            case 'м':  base_to = 1.0
            case 'км': base_to = 1000.0

    case '3':
        print("Доступные единицы: сек, мин, ч")
        units = input("Введите исходную и целевую единицу через пробел (например, ч мин): ").split()
        val = float(input("Введите значение: "))
        
        from_u, to_u = units[0], units[1]
        
        # Базовая единица — секунда
        match from_u:
            case 'сек': base_from = 1.0
            case 'мин': base_from = 60.0
            case 'ч':   base_from = 3600.0

        match to_u:
            case 'сек': base_to = 1.0
            case 'мин': base_to = 60.0
            case 'ч':   base_to = 3600.0

    case _:
        print("Неверный ключ категории!")

if base_from == 0.0 or base_to == 0.0:
    print("Ошибка: введены неподдерживаемые единицы измерения.")
else:
    result = (val * base_from) / base_to
    print(f"Результат: {val} {from_u} = {result} {to_u}")
