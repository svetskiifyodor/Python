from PIL import Image, ImageDraw, ImageFont

# Открытие исходного изображения
image = Image.open('your_image.jpg')

# Создание объекта для рисования на изображении
draw = ImageDraw.Draw(image)

# Добавление текстового водяного знака
text = "Watermark Text"
font = ImageFont.load_default()  # Вы можете использовать свой шрифт, если хотите

# Позиция текста на изображении (например, внизу справа)
text_position = (image.width - 200, image.height - 50)

# Цвет текста (белый)
text_color = (255, 255, 255)

# Добавление текста
draw.text(text_position, text, font=font, fill=text_color)

# Открытие изображения для водяного знака (например, логотип)
watermark_image = Image.open('watermark.png')

# Уменьшение размера водяного знака
watermark_image = watermark_image.resize((100, 100))  # Можно изменить размер по вашему усмотрению

# Позиция водяного знака на изображении (например, внизу справа)
watermark_position = (image.width - 120, image.height - 120)

# Наложение водяного знака
image.paste(watermark_image, watermark_position, watermark_image)

# Отображение результата
image.show()

# Сохранение изображения в формате JPG
image.save('output_image.jpg', 'JPEG')
