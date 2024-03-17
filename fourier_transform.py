import numpy as np
import matplotlib.pyplot as plt

def fourier_transform(f, t, omega):
    F_omega = np.zeros_like(omega, dtype=complex)
    for i, w in enumerate(omega):
        F_omega[i] = np.sum(f(t) * np.exp(-2*1j*w*t)) * (t[1]-t[0])
    return F_omega

def fourier_graph(f):
    t = np.linspace(-20, 20, 1000)
    omega = np.linspace(-20, 20, 1000)
    F_omega = fourier_transform(f, t, omega)
    plt.figure(figsize=(10, 6))
    plt.plot(omega, np.abs(F_omega), label='')
    plt.xlabel('Частота (ω)')
    plt.ylabel('Амплитуда')
    plt.title('График Фурье-образа функции f(ω)')
    plt.legend()
    plt.grid(True)
    plt.show()