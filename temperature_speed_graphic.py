import matplotlib.pyplot as plt
from math import sqrt


t0 = 227.2
v0 = 236.1
temperature_x = [273 - 41, 273 - 35, 273 - 5, 273 + 19.7]
speed_y = [(v0 * sqrt(i)) / sqrt(t0) for i in temperature_x]
plt.plot(temperature_x, speed_y)
plt.xlabel('x - температура, К')
plt.ylabel('y - скорость, м/с')
plt.title('Зависимость скорости от температуры')
plt.show()
