import os
import sys
from PIL import Image


def create_thumbnail(image_path, size=(50, 50)):
    try:
        # Открытие изображения
        img = Image.open(image_path)

        # Создание эскиза (уменьшение изображения)
        img.thumbnail(size)

        # Отображение эскиза
        img.show()
    except Exception as e:
        print(f"Ошибка при обработке изображения {image_path}: {e}")


def main():
    # Получаем путь к файлу из аргументов командной строки
    if len(sys.argv) != 3 or sys.argv[1] != "-ft":
        print("Использование: python script.py -ft <file_extension>")
        sys.exit(1)

    file_extension = sys.argv[2].lower()
    supported_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")

    # Проверка на поддерживаемое расширение
    if file_extension not in supported_extensions:
        print(f"Расширение {file_extension} не поддерживается.")
        sys.exit(1)

    # Получаем все файлы с данным расширением в текущей директории
    files = [f for f in os.listdir() if f.lower().endswith(file_extension)]

    if not files:
        print(f"Не найдено файлов с расширением {file_extension}.")
        sys.exit(1)

    # Создание эскизов для каждого найденного файла
    for file in files:
        print(f"Создание эскиза для файла {file}...")
        create_thumbnail(file)


if __name__ == "__main__":
    main()
