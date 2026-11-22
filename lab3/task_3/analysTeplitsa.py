import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize, integrate

# 1. Исходные данные с пропусками (время в часах от 0 до 23 и температура в °C)
hours_raw = np.array([0, 2, 5, 8, 11, 13, 15, 18, 20, 23], dtype=float)
temps_raw = np.array([17.5, 16.2, 15.8, 18.5, 22.8, 25.4, 26.1, 23.2, 20.4, 18.0], dtype=float)

NORM_TEMP = 22.0

# Базовая проверка входных данных
if len(hours_raw) != len(temps_raw) or len(hours_raw) < 4:
    raise ValueError("Массивы времени и температуры должны быть одной длины (минимум 4 точки).")
if not np.all(np.diff(hours_raw) > 0):
    raise ValueError("Время должно идти строго по возрастанию без дубликатов.")

t_start, t_end = hours_raw[0], hours_raw[-1]

# 2. Восстановление температуры на каждый час (scipy.interpolate)
temp_func = interpolate.CubicSpline(hours_raw, temps_raw)

all_hours = np.arange(0, 24, 1)
hourly_temps = temp_func(all_hours)

print("     ВОССТАНОВЛЕННАЯ ТЕМПЕРАТУРА ПО ЧАСАМ    ")
for h, t in zip(all_hours, hourly_temps):
    mark = " (исходная)" if h in hours_raw else ""
    print(f"{int(h):02d}:00 -> {t:.2f} °C{mark}")

# 3. Поиск минимума и максимума температуры (scipy.optimize)
res_min = optimize.minimize_scalar(temp_func, bounds=(t_start, t_end), method="bounded")
res_max = optimize.minimize_scalar(lambda x: -temp_func(x), bounds=(t_start, t_end), method="bounded")

if not (res_min.success and res_max.success):
    raise RuntimeError("Не удалось найти минимум или максимум температуры.")

t_min, val_min = res_min.x, res_min.fun
t_max, val_max = res_max.x, -res_max.fun


def format_time(hours_float: float) -> str:
    h = int(hours_float)
    m = int(round((hours_float - h) * 60))
    if m == 60:
        h += 1
        m = 0
    return f"{h:02d}:{m:02d}"


print("\n    ЭКСТРЕМУМЫ ЗА ДЕНЬ     ")
print(f"Минимальная температура: {val_min:.2f} °C в {format_time(t_min)} ({t_min:.2f} ч)")
print(f"Максимальная температура: {val_max:.2f} °C в {format_time(t_max)} ({t_max:.2f} ч)")

# 4. Средняя температура за день (scipy.integrate)
area, _ = integrate.quad(temp_func, t_start, t_end)
avg_temp = area / (t_end - t_start)

print(f"\n     СРЕДНЯЯ ТЕМПЕРАТУРА ЗА ДЕНЬ     ")
print(f"Средняя температура: {avg_temp:.2f} °C")

# 5. Точное время пересечения отметки 22°C (scipy.optimize.root_scalar)
crossings = []
for i in range(len(all_hours) - 1):
    a, b = float(all_hours[i]), float(all_hours[i + 1])
    fa = temp_func(a) - NORM_TEMP
    fb = temp_func(b) - NORM_TEMP

    if fa * fb <= 0:
        try:
            root_res = optimize.root_scalar(
                lambda x: temp_func(x) - NORM_TEMP,
                bracket=[a, b],
                method="brentq",
            )
            if root_res.converged:
                crossings.append(root_res.root)
        except ValueError:
            continue

print(f"\n    ПЕРЕСЕЧЕНИЕ НОРМЫ ({NORM_TEMP:.0f} °C)    ")
if crossings:
    for t_cross in crossings:
        print(f"Температура пересекла {NORM_TEMP:.0f} °C в {format_time(t_cross)} ({t_cross:.2f} ч)")
else:
    print(f"Температура за день не пересекала отметку {NORM_TEMP:.0f} °C.")

# 6. Построение графика
t_smooth = np.linspace(t_start, t_end, 300)
temp_smooth = temp_func(t_smooth)

plt.figure(figsize=(10, 6))
plt.plot(t_smooth, temp_smooth, label="Восстановленная кривая (CubicSpline)", color="steelblue", linewidth=2)
plt.scatter(hours_raw, temps_raw, label="Исходные данные датчика", color="black", zorder=5)
plt.scatter([t_min], [val_min], label=f"Минимум ({val_min:.1f} °C в {format_time(t_min)})", color="blue", s=90, zorder=6)
plt.scatter([t_max], [val_max], label=f"Максимум ({val_max:.1f} °C в {format_time(t_max)})", color="red", s=90, zorder=6)
plt.axhline(NORM_TEMP, color="orange", linestyle="--", linewidth=1.8, label=f"Норма ({NORM_TEMP:.0f} °C)")

if crossings:
    plt.scatter(crossings, [NORM_TEMP] * len(crossings), color="green", s=70, zorder=6, label="Пересечение нормы")

plt.title("Аналитика температуры в теплице за сутки")
plt.xlabel("Время (часы)")
plt.ylabel("Температура (°C)")
plt.xticks(range(0, 24, 2))
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("greenhouse_temp.png", dpi=150)
plt.show()