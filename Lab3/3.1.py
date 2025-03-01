import os
from PIL import Image, ImageEnhance, ImageFilter
import random
import sys


# Функции для атомарных преобразований
def rotate_image(image):
    return image.rotate(random.randint(0, 360))


def flip_image(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def adjust_brightness(image):
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(0.5, 1.5)  # Изменение яркости
    return enhancer.enhance(factor)


def apply_blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.5, 2)))


def resize_image(image):
    new_size = (random.randint(100, 400), random.randint(100, 400))
    return image.resize(new_size)


# Комплексное преобразование: сочетание нескольких атомарных преобразований
def complex_transformation(image):
    image = rotate_image(image)
    image = flip_image(image)
    image = adjust_brightness(image)
    return image


# Функция для аугментации изображений в папке
def augment_images(folder_path, transformations, num_images=20):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    image_files = image_files[:num_images]  # Берем только первые 20 изображений

    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)

        # Выбираем случайную комбинацию преобразований
        for transformation in transformations:
            image = transformation(image)

        # Сохраняем результат в исходную папку с новыми именами
        new_image_name = f"{idx + 1}.jpg"  # Непрерывная нумерация
        image.save(os.path.join(folder_path, new_image_name))
        print(f"Изображение сохранено: {new_image_name}")


# Основной блок программы
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Необходимо указать путь к папке с изображениями!")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Список доступных преобразований
    transformations = []
    print("Выберите преобразования для аугментации (введите номера через запятую):")
    print("1. Поворот")
    print("2. Отражение по горизонтали")
    print("3. Коррекция яркости")
    print("4. Размытие")
    print("5. Изменение размера")
    print("6. Комплексное преобразование (все сразу)")

    selected = input().split(',')
    if '1' in selected:
        transformations.append(rotate_image)
    if '2' in selected:
        transformations.append(flip_image)
    if '3' in selected:
        transformations.append(adjust_brightness)
    if '4' in selected:
        transformations.append(apply_blur)
    if '5' in selected:
        transformations.append(resize_image)
    if '6' in selected:
        transformations.append(complex_transformation)

    # Запуск аугментации
    augment_images(folder_path, transformations)
    print("Аугментация завершена.")
