import os

def check_files_in_directory(dirpath: str = "./", *files: str):
    dirpath = os.path.abspath(dirpath)
    present_files = []
    absent_files = []

    # Проверка существования файлов в папке
    for file in files:
        full_path = os.path.join(dirpath, file)
        if os.path.isfile(full_path):
            present_files.append(file)
        else:
            absent_files.append(file)

    # Вывод и запись в файлы
    present_file_path = os.path.join(dirpath, "present_files.txt")
    absent_file_path = os.path.join(dirpath, "absent_files.txt")

    with open(present_file_path, "w") as present_file:
        for file in present_files:
            present_file.write(file + "\n")

    with open(absent_file_path, "w") as absent_file:
        for file in absent_files:
            absent_file.write(file + "\n")

    print("Список присутствующих файлов:")
    for file in present_files:
        print(file)

    print("\nСписок отсутствующих файлов:")
    for file in absent_files:
        print(file)


if __name__ == "__main__":
    dirpath = input("Введите путь к папке (или оставьте пустым для текущей папки): ").strip() or "./"
    files = input("Введите имена файлов через пробел: ").strip().split()
    check_files_in_directory(dirpath, *files)
