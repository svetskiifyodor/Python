from moviepy.editor import VideoFileClip

def extract_video_segment(input_file, start_time, end_time, output_file):
    try:
        # Загружаем видеофайл
        video = VideoFileClip(input_file)

        # Извлекаем фрагмент с указанного времени
        video_segment = video.subclip(start_time, end_time)

        # Сохраняем извлеченный фрагмент в новый файл
        video_segment.write_videofile(output_file, codec="libx264")

        print(f"Фрагмент успешно сохранен как {output_file}")

    except Exception as e:
        print(f"Ошибка: {e}")

# Получаем параметры от пользователя
input_file = input("Введите имя входного видеофайла: ")  # Входной файл
start_time = tuple(map(int, input("Введите время начала фрагмента (часы, минуты, секунды): ").split(',')))  # Время начала фрагмента
end_time = tuple(map(int, input("Введите время окончания фрагмента (часы, минуты, секунды): ").split(',')))  # Время окончания фрагмента
output_file = input("Введите имя выходного видеофайла: ")  # Имя выходного файла

extract_video_segment(input_file, start_time, end_time, output_file)
