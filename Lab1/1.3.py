import os
from pathlib import Path

def check_files_in_directory(dirpath=".", *files):
    dirpath = Path(dirpath)  # Преобразование в объект Path
    present_files = []  # Список файлов, которые есть в папке
    absent_files = []   # Список файлов, которых нет в папке

    if files:
        # Проверка наличия переданных файлов в папке
        for file in files:
            file_path = dirpath / file
            if file_path.exists() and file_path.is_file():
                present_files.append(file)
            else:
                absent_files.append(file)

        # Запись результатов в файлы
        with open("present_files.txt", "w") as present_file:
            present_file.write("\n".join(present_files))
        with open("absent_files.txt", "w") as absent_file:
            absent_file.write("\n".join(absent_files))

        # Вывод списков на экран
        print("Файлы, найденные в папке:")
        print("\n".join(present_files) if present_files else "Нет найденных файлов.")

        print("\nФайлы, отсутствующие в папке:")
        print("\n".join(absent_files) if absent_files else "Все файлы присутствуют.")

    else:
        # Если файлы не переданы, вывод общей информации о папке
        total_size = sum(f.stat().st_size for f in dirpath.glob("*") if f.is_file())
        total_files = len([f for f in dirpath.iterdir() if f.is_file()])
        print(f"Общая информация о папке '{dirpath}':")
        print(f"Количество файлов: {total_files}")
        print(f"Общий размер файлов: {total_size} байт")

if __name__ == "__main__":
    dirpath = input("Введите путь к папке (по умолчанию текущая папка): ").strip() or "."
    files_input = input("Введите имена файлов через пробел (или оставьте пустым): ").strip().split()
    check_files_in_directory(dirpath, *files_input)
