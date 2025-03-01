from PIL import Image, ImageDraw, ImageFont


# Функция для создания карточки
def create_card(number):
    # Создание пустого изображения (белый фон)
    card = Image.new('RGB', (100, 100), (255, 255, 255))

    # Создание объекта для рисования
    draw = ImageDraw.Draw(card)

    # Рисуем синюю рамку
    frame_thickness = 5
    draw.rectangle([0, 0, 100, 100], outline="blue", width=frame_thickness)  # Сразу рисуем рамку по всему краю

    # Рисуем текст (цифры) в центре
    font = ImageFont.load_default()  # Можно использовать свой шрифт
    text = str(number)

    # Получаем размер текста с помощью textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_position = ((100 - text_width) // 2, (100 - text_height) // 2)

    # Рисуем красный текст
    draw.text(text_position, text, font=font, fill="red")

    return card


# Создание трех карточек
cards = [create_card(1), create_card(2), create_card(3)]

# Отображение карточек
for card in cards:
    card.show()

# Сохранение карточек в формате PNG
for i, card in enumerate(cards, 1):
    card.save(f'card_{i}.png', 'PNG')
