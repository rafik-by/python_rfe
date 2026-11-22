from functools import *
import time


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwangs):
        start_time = time.perf_counter()

        result = func(*args,**kwangs)

        end_time = time.perf_counter()
        #переведем в милисекунды
        full_time = (end_time-start_time)*1000
        print(f"Функция {func.__name__} выполнилась за время {full_time:3f}")

        return result
    return wrapper

@timing
def multiply(a,b,c):
    result = a*b*c
    return result

print(f"запуск {multiply(1,2,3)}",
      f"запуск {multiply(12,23,34)}",
      f"запуск {multiply(16,27,38)}",
      f"запуск {multiply(100,223,3112)}",
        sep = "\n")

