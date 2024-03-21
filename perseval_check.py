import numpy as np

def f(t):
    if(abs(t) <= 2):
        return (1 - abs(1*t/2))
    elif(abs(t) > 2):
        return 0


def fourier_transform(f, x, xi):
    F_xi = np.zeros_like(xi, dtype=complex)
    for i, w in enumerate(xi):
        F_xi[i] = np.sum(f(x) * np.exp(-2 * 1j * np.pi * w * x)) * (x[1] - x[0])
    return F_xi

def parseval_second_norm(f, x, xi):
    F_xi = fourier_transform(f, x, xi)

    norm_squared_time = np.trapz(np.abs(f(x)) ** 2, x)
    norm_squared_freq = np.trapz(np.abs(F_xi) ** 2, xi)

    return norm_squared_time, norm_squared_freq

# Генерация значений для x и xi
x = np.linspace(-10, 10, 1000)
xi = np.linspace(-10, 10, 1000)

# Вычисление равенства Парсеваля для второй нормы
norm_time, norm_freq = parseval_second_norm(f, x, xi)
print("Вторая норма функции:", norm_time)
print("Вторая норма её Фурье-образа:", norm_freq)