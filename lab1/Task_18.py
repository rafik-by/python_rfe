from functools import * 
from datetime import *


def log_calls(filename):
    def decorator(func):
        @wraps(func)
        def wraper(*args,**kwangs):
            current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

            pos_args = [repr(arg) for arg in args]
            pos_kwags = [f"{key}: {repr(value)}" for key , value in kwangs.items()]
            format_args = " ,".join(pos_args + pos_kwags)

            log_line = f"{current_date} Вызвана функция {func.__name__}({format_args})\n"

            with open(filename, mode='a', encoding='utf-8') as log_file:
                log_file.write(log_line)
            
            return func(*args, **kwangs)
        return wraper
    return decorator

LOG_FILENAME = "Python.txt"

@log_calls(LOG_FILENAME)
def call(name):
    return f'Звонок от {name}'



print(call('Вадим'))
print(call('Николай'))
print(call('Матвей'))

print(f"Содержимое файла {LOG_FILENAME}")
with open(LOG_FILENAME, mode="r", encoding="utf-8") as file:
    print(file.read(), end="")

with open(LOG_FILENAME, mode= 'w', encoding='utf-8') as file:
    pass

