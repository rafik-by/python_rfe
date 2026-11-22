from functools import *

def type_check(*all_param):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwangs):
            all_args = list(args) + list(kwangs.values())

            if len(all_param) != len(all_args):
                raise TypeError(
                    f"Длина исходного проверяемого числа параметров{len(all_param)}, не совпадает с переданным значение{len(all_args)}")

            for i in range(len(all_args)):
                current_arg = all_args[i]
                current_param = all_param[i]

                if not isinstance(current_arg, current_param):
                    raise TypeError(
                        f"Ошибка типа в '{func.__name__}'! Аргумент №{i + 1} со значением "
                        f"{repr(current_arg)} имеет тип '{type(current_arg).__name__}', "
                        f"а требовался тип '{current_param.__name__}'."
                    )
            print(f"[Проверка типов] Все аргументы для '{func.__name__}' корректны: {all_args}"
            )
            return func(*args, **kwangs)

        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b


@type_check(str, int)
def repeat_word(word, times):
    return word * times



print(f"Результат add(10, 25): {add(10, 25)}\n")
print(f"Результат repeat_word('Питон! ', 3): {repeat_word('Питон! ', 3)}\n")
        