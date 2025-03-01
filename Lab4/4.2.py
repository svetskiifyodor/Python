import os
from moviepy.editor import VideoFileClip
from PIL import Image  # Импортируем модуль Image для работы с изображениями


def extract_frames(input_file, start_time, end_time, output_folder, step=10):
    try:
        # Загружаем видеофайл
        video = VideoFileClip(input_file)

        # Извлекаем фрагмент
        video_segment = video.subclip(start_time, end_time)

        # Создаем папку для сохранения кадров, если её нет
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Извлекаем кадры с заданным шагом
        frame_number = 0
        for t in range(0, int(video_segment.duration), step):
            frame = video_segment.get_frame(t)  # Получаем кадр на момент времени t
            frame_file = os.path.join(output_folder, f"frame_{frame_number}.png")
            # Сохраняем кадр
            frame_img = Image.fromarray(frame)
            frame_img = frame_img.resize(
                (250, int(frame.shape[0] * 250 / frame.shape[1])))  # Изменяем размер кадра по горизонтали
            frame_img.save(frame_file)
            print(f"Кадр сохранен: {frame_file}")
            frame_number += 1

        print("Извлечение кадров завершено.")

    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования функции
input_file = input("Введите имя входного видеофайла: ")  # Входной файл
start_time = tuple(
    map(int, input("Введите время начала фрагмента (часы, минуты, секунды): ").split(',')))  # Время начала фрагмента
end_time = tuple(map(int, input("Введите время окончания фрагмента (часы, минуты, секунды): ").split(
    ',')))  # Время окончания фрагмента
output_folder = input("Введите путь для записи кадров: ")  # Папка для сохранения кадров
step = int(input("Введите шаг извлечения кадров (по умолчанию 10): ") or 10)  # Шаг извлечения кадров

extract_frames(input_file, start_time, end_time, output_folder, step)
