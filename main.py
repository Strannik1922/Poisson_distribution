import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from scipy.optimize import minimize


# Задаем параметры распределения Пуассона
mu = 1.8

# Генерируем случайные величины с распределением Пуассона для размеров покупок
purchase_sizes = np.random.poisson(mu, 100)

# Установим максимальную скидку
max_discount = 30  # Можно изменить на любое другое число

# Определить функцию, которую нужно минимизировать
def objective(x):
    a, b = x
    return ((b + a) / 2 - max_discount / 3 * 0.75) ** 2 + (b - a - max_discount) ** 2

# Определить границы для a и b
bnds = [(0, max_discount), (0, max_discount)]

# Определить начальную точку
x0 = [0, max_discount]

# Использовать метод L-BFGS-B, чтобы минимизировать функцию
res = minimize(objective, x0, method='L-BFGS-B', bounds=bnds)

# Получить результаты
a, b = res.x

# Используем полученные коэффициенты для генерации скидок с равномерным распределением
discounts = np.random.uniform(a, b, len(purchase_sizes))

# Выведем полученные скидки
for i, discount in enumerate(discounts):
    print(f"Purchase size: {purchase_sizes[i]}, Discount: {discount:.2f}%")


sb.set_style('whitegrid')
plt.vlines(purchase_sizes ,0, discounts, colors='k', linestyle='-', lw=6)
plt.ylabel('Discount, %')
plt.xlabel('Purchase size, pcs')
plt.show()
