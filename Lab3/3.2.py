import sys
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# Функция для отображения гистограммы
def plot_histogram(image, title, ax):
    r, g, b = image.split()

    # Получаем данные для каждого канала
    r_hist = np.array(r).ravel()
    g_hist = np.array(g).ravel()
    b_hist = np.array(b).ravel()

    # Строим гистограммы для каждого канала с цветами
    ax.hist(r_hist, bins=256, color='red', alpha=0.7, label='R')
    ax.hist(g_hist, bins=256, color='green', alpha=0.7, label='G')
    ax.hist(b_hist, bins=256, color='blue', alpha=0.7, label='B')
    ax.set_title(title)
    ax.set_xlim(0, 255)
    ax.legend()


# Основной блок программы
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Необходимо указать путь к изображению!")
        sys.exit(1)

    image_path = sys.argv[1]

    # Загружаем изображение
    image = Image.open(image_path)

    # Настройка графиков с использованием gridspec
    fig = plt.figure(figsize=(14, 20))

    # Определяем grid: 1 строка для изображения и 4 строки для гистограмм
    gs = fig.add_gridspec(5, 2, width_ratios=[3, 1])  # 5 строк, 2 столбца

    # Первая ячейка: изображение
    ax1 = fig.add_subplot(gs[0:5, 0])  # изображение занимает 5 строк
    ax1.imshow(image)
    ax1.axis('off')  # Убираем оси
    ax1.set_title("Исходное изображение")

    # Вторая ячейка: гистограммы
    # Гистограмма для всего изображения (цветная)
    ax2 = fig.add_subplot(gs[0, 1])
    plot_histogram(image, "Гистограмма изображения", ax2)

    # Гистограмма для канала R
    ax3 = fig.add_subplot(gs[1, 1])
    r, _, _ = image.split()
    ax3.hist(np.array(r).ravel(), bins=256, color='red', alpha=0.7)
    ax3.set_title("Гистограмма канала R")
    ax3.set_xlim(0, 255)

    # Гистограмма для канала G
    ax4 = fig.add_subplot(gs[2, 1])
    _, g, _ = image.split()
    ax4.hist(np.array(g).ravel(), bins=256, color='green', alpha=0.7)
    ax4.set_title("Гистограмма канала G")
    ax4.set_xlim(0, 255)

    # Гистограмма для канала B
    ax5 = fig.add_subplot(gs[3, 1])
    _, _, b = image.split()
    ax5.hist(np.array(b).ravel(), bins=256, color='blue', alpha=0.7)
    ax5.set_title("Гистограмма канала B")
    ax5.set_xlim(0, 255)

    # Показываем результаты
    plt.tight_layout()
    plt.show()
