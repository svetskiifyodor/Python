import os
import shutil


def find_and_copy_small_files(directory="."):
    small_files = []
    small_folder = os.path.join(directory, "small")

    # Проверка всех файлов в указанной папке
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) < 2048:  # Проверяем размер меньше 2К
                small_files.append(file_path)

    if small_files:
        print("Найдены следующие файлы меньше 2К:")
        for file in small_files:
            print(file)

        # Создание папки для маленьких файлов, если она не существует
        os.makedirs(small_folder, exist_ok=True)

        # Копирование файлов в папку "small"
        for file in small_files:
            destination = os.path.join(small_folder, os.path.basename(file))
            shutil.copy2(file, destination)
        print(f"Все файлы скопированы в папку: {small_folder}")
    else:
        print("Файлы размером меньше 2К отсутствуют.")


if __name__ == "__main__":
    directory = input("Введите путь к папке (или оставьте пустым для текущей папки): ").strip()
    directory = directory if directory else "."
    find_and_copy_small_files(directory)
