import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # Количество точек
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.5)

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Показ графика
plt.show()