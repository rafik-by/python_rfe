from functools import *

def cache(func):
    dict_cache ={}
    @wraps(func)
    def wrapper(*args, **kwangs):
        cache_keys = (args, tuple(kwangs.items()))
        if cache_keys in dict_cache:
            print(f"Аргументы {args} {kwangs if kwangs else ''} уже известны! ",
                f"Берем готовый ответ из памяти: {dict_cache[cache_keys]}")
            return dict_cache 
        result = func(*args,**kwangs)
        dict_cache[cache_keys] = result
        return result
    return wrapper


@cache
def heavy_multiply(a, b, bonus=0):
    return a * b + bonus


print(f"Итог вызова: {heavy_multiply(5, 10)}\n")
print(f"Итог вызова: {heavy_multiply(5, 10)}\n")
print(f"Итог вызова: {heavy_multiply(2, 3, bonus=10)}\n")
print(f"Итог вызова: {heavy_multiply(2, 3, bonus=10)}")
