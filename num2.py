import matplotlib.pyplot as plt

def fourier_transform(f, t, omega):
    F_omega = np.zeros_like(omega, dtype=complex)
    for i, w in enumerate(omega):
        F_omega[i] = np.sum(f(t) * np.exp(-2*1j*w*t)) * (t[1]-t[0])
    return F_omega
def plot_fourier_transform(f):
    t = np.linspace(-20, 20, 1000)
    omega = np.linspace(-20, 20, 1000)
    F_omega = fourier_transform(f, t, omega)

    zero_array = np.zeros_like(omega)  # Создаем массив нулей той же длины, что и omega

    plt.figure(figsize=(15, 10))

    plt.subplot(311)
    plt.plot(omega, F_omega.real, label='Re gˆ(ω)')
    plt.xlabel('Частота (ω)')
    plt.ylabel('Re gˆ(ω)')
    plt.title('Вещественная часть Фурье-образа')

    plt.subplot(312)
    plt.plot(omega, zero_array, label='Im gˆ(ω)')  # Используем zero_array вместо g(t)
    plt.xlabel('Частота (ω)')
    plt.ylabel('Im gˆ(ω)')
    plt.title('Мнимая часть Фурье-образа')

    plt.subplot(313)
    plt.plot(omega, np.abs(F_omega), label='|gˆ(ω)|')
    plt.xlabel('Частота (ω)')
    plt.ylabel('|gˆ(ω)|')
    plt.title('Модуль Фурье-образа')

    plt.tight_layout()
    plt.show()

plot_fourier_transform(f)