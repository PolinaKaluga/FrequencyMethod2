import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.fft import fft, fftfreq

# Загрузка аудиофайла и преобразование в массив
audio_file = '/Users/polinakalugina/Desktop/итмо юниверсити/21.mp3'
y, sr = librosa.load(audio_file)

# Построение графика f(t)
plt.figure(figsize=(15, 5))
plt.plot(np.arange(len(y)) / sr, y)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.title('График аудиозаписи')
plt.show()

# Вычисление Фурье-образа f(ν) с использованием численного интегрирования
V = sr / 2
dv = 1
v = np.arange(0, V, dv)
Y = np.zeros(len(v), dtype=complex)

for k in range(len(v)):
    Y[k] = np.trapz(y * np.exp(-1j * 2 * np.pi * v[k] * np.arange(len(y)) / sr))

# Построение графика |f(ν)|
plt.figure(figsize=(10, 5))
plt.plot(v, np.abs(Y))
plt.xlabel('Частота (Гц)')
plt.ylabel('|f(ν)|')
plt.title('График модуля Фурье-образа')
plt.show()