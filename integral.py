import numpy as np
from scipy.integrate import quad

def fourier_transform_integral(a, b):
    def f(t):
        return a * np.exp(-b * abs(t))

    def integrand(t, w):
        return f(t) * np.exp(- 1j * w * t)

    def fourier_transform(w):
        integral_result, _ = quad(integrand, -np.inf, np.inf, args=(w))
        return integral_result

    return fourier_transform

# Заданные параметры a и b
a = 1
b = 2

# Вычисление интеграла Фурье-образа для заданных параметров
integral_result = fourier_transform_integral(a, b)
print("Интеграл Фурье-образа для функции a * sinc(b * t):", integral_result(0.2))  # Пример вычисления для w=1.0