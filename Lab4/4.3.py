import cv2


def play_video_with_info(input_file):
    # Загружаем видеофайл
    video = cv2.VideoCapture(input_file)

    if not video.isOpened():
        print("Ошибка при открытии видеофайла")
        return

    # Получаем параметры видео
    fps = video.get(cv2.CAP_PROP_FPS)  # Количество кадров в секунду
    video_name = input_file.split("\\")[-1]  # Имя файла

    while True:
        # Читаем кадры из видео
        ret, frame = video.read()

        if not ret:
            break

        # Добавляем текст на кадр (имя файла и fps)
        cv2.putText(frame, f"Video: {video_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f"FPS: {fps}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Показываем кадр
        cv2.imshow('Video', frame)

        # Выход из видео по нажатию клавиши 'q'
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    # Освобождаем ресурсы
    video.release()
    cv2.destroyAllWindows()


# Пример использования
input_file = input("Введите имя видеофайла: ")  # Входной файл
play_video_with_info(input_file)
