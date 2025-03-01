import librosa
import librosa.display
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Загружаем аудио файл
audio_data = 'test.mp3'  # Замените на путь к вашему файлу
y, sr = librosa.load(audio_data)

# Отображаем амплитудно-временную форму сигнала
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('Амплитудно-временная форма сигнала')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.show()

# Преобразование Фурье для частотного спектра (анализ одного момента времени)
D = np.abs(librosa.stft(y))  # Преобразование Фурье для одного кадра
plt.figure(figsize=(12, 4))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
plt.title('Частотный спектр в один момент времени')
plt.colorbar(format='%+2.0f dB')
plt.xlabel('Время (с)')
plt.ylabel('Частота (Гц)')
plt.show()

# Построение спектрограммы (анализ всего сигнала по времени)
plt.figure(figsize=(12, 4))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Спектрограмма сигнала')
plt.xlabel('Время (с)')
plt.ylabel('Частота (Гц)')
plt.show()


# Вычисление темпа и битов
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f"Темп: {tempo} bpm")
print(f"Количество битов: {len(beat_frames)}")

# Мел-кепстральные коэффициенты (MFCC)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
plt.figure(figsize=(12, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.title('Мел-кепстральные коэффициенты (MFCC)')
plt.colorbar()
plt.xlabel('Время (с)')
plt.ylabel('Коэффициенты')
plt.show()

# Спектральный центроид
spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

# Нормализуем спектральный центроид
scaler = MinMaxScaler()
normalized_centroids = scaler.fit_transform(spectral_centroids.reshape(-1, 1))

# Визуализация спектрального центроида
plt.figure(figsize=(12, 4))
frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)
librosa.display.waveshow(y, sr=sr, alpha=0.4)
plt.plot(t, normalized_centroids, color='b')
plt.title('Спектральный центроид и форма волны')
plt.xlabel('Время (с)')
plt.ylabel('Нормализованный спектральный центроид')
plt.show()
