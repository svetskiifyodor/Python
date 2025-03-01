import sys
from PIL import Image


def most_used_color(image_path):
    # Открытие изображения
    image = Image.open(image_path)

    # Получение данных пикселей
    pixels = list(image.getdata())

    # Инициализация счетчиков для каналов R, G, B
    r_count, g_count, b_count = 0, 0, 0

    # Подсчет каждого канала (R, G, B) в изображении
    for r, g, b in pixels:
        r_count += r
        g_count += g
        b_count += b

    # Определение самого используемого цвета
    if r_count > g_count and r_count > b_count:
        return "Красный (R)"
    elif g_count > r_count and g_count > b_count:
        return "Зеленый (G)"
    else:
        return "Синий (B)"


if __name__ == "__main__":
    # Проверка на наличие системного параметра
    if len(sys.argv) < 2:
        print("Необходимо передать путь к изображению как системный параметр.")
        sys.exit(1)

    # Получение пути к изображению из параметров
    image_path = sys.argv[1]

    # Вычисление и вывод результата
    result = most_used_color(image_path)
    print(f"Цвет, используемый больше всего: {result}")
