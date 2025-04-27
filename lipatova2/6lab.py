import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Создание переменных
temperature = ctrl.Antecedent(np.arange(15, 31, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(30, 81, 1), 'humidity')
time_of_day = ctrl.Antecedent(np.arange(0, 25, 1), 'time_of_day')
power = ctrl.Consequent(np.arange(0, 101, 1), 'power')

# Функции принадлежности для температуры
temperature['cold'] = fuzz.trimf(temperature.universe, [15, 15, 20])
temperature['comfortable'] = fuzz.trimf(temperature.universe, [18, 22, 25])
temperature['hot'] = fuzz.trimf(temperature.universe, [23, 30, 30])

# Функции принадлежности для влажности
humidity['dry'] = fuzz.trimf(humidity.universe, [30, 30, 50])
humidity['normal'] = fuzz.trimf(humidity.universe, [40, 55, 70])
humidity['humid'] = fuzz.trimf(humidity.universe, [60, 80, 80])

# Функции принадлежности для времени суток
time_of_day['night'] = fuzz.trimf(time_of_day.universe, [0, 0, 6])
time_of_day['morning'] = fuzz.trimf(time_of_day.universe, [5, 8, 11])
time_of_day['day'] = fuzz.trimf(time_of_day.universe, [10, 14, 18])
time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [17, 20, 24])

# Функции принадлежности для мощности
power['off'] = fuzz.trimf(power.universe, [0, 0, 30])
power['low'] = fuzz.trimf(power.universe, [20, 40, 60])
power['medium'] = fuzz.trimf(power.universe, [50, 70, 90])
power['high'] = fuzz.trimf(power.universe, [80, 100, 100])

# Визуализация функций принадлежности
temperature.view()
plt.title('Функции принадлежности для температуры')
plt.show()

humidity.view()
plt.title('Функции принадлежности для влажности')
plt.show()

time_of_day.view()
plt.title('Функции принадлежности для времени суток')
plt.show()

power.view()
plt.title('Функции принадлежности для мощности обогревателя')
plt.show()

# Создание правил
rule1 = ctrl.Rule(temperature['cold'] & humidity['dry'], power['high'])
rule2 = ctrl.Rule(temperature['comfortable'] & time_of_day['night'], power['low'])
rule3 = ctrl.Rule(temperature['hot'] | humidity['humid'], power['off'])

# Создание системы управления
heating_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
heating = ctrl.ControlSystemSimulation(heating_ctrl)

# 1-й прогон: холодно и сухо
heating.input['temperature'] = 16
heating.input['humidity'] = 35
heating.input['time_of_day'] = 10  # день
heating.compute()
print(f"1-й прогон (16°C, 35% влажности, день): мощность = {heating.output['power']:.2f}%")
power.view(sim=heating)
plt.show()

# 2-й прогон: комфортно ночью
heating.input['temperature'] = 21
heating.input['humidity'] = 50
heating.input['time_of_day'] = 2  # ночь
heating.compute()
print(f"2-й прогон (21°C, 50% влажности, ночь): мощность = {heating.output['power']:.2f}%")
power.view(sim=heating)
plt.show()

# 3-й прогон: жарко и влажно
heating.input['temperature'] = 28
heating.input['humidity'] = 75
heating.input['time_of_day'] = 15  # день
heating.compute()
print(f"3-й прогон (28°C, 75% влажности, день): мощность = {heating.output['power']:.2f}%")
power.view(sim=heating)
plt.show()

# Построение поверхности нечёткого вывода
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Фиксируем время суток (день - 12 часов)
x = np.arange(15, 31, 1)
y = np.arange(30, 81, 1)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        try:
            heating.input['temperature'] = x[i]
            heating.input['humidity'] = y[j]
            heating.input['time_of_day'] = 12  # фиксируем день
            heating.compute()
            Z[j, i] = heating.output['power']  # убедитесь, что ключ 'power' существует
        except KeyError:
            print(f"Ошибка при температуре {x[i]} и влажности {y[j]}")
            Z[j, i] = 0

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
ax.set_xlabel('Температура (°C)')
ax.set_ylabel('Влажность (%)')
ax.set_zlabel('Мощность (%)')
ax.set_title('Поверхность нечёткого вывода (время суток = день)')
plt.show()