from PIL import Image
import matplotlib.pyplot as plt

# Открытие исходного изображения
image_path = 'your_image.jpg' 
image = Image.open(image_path)

# Разделение каналов R, G и B
r, g, b = image.split()

# Настройка фигуры для отображения изображений
fig, axes = plt.subplots(1, 4, figsize=(16, 8))

# Отображение исходного изображения
axes[0].imshow(image)
axes[0].set_title('Исходное изображение')
axes[0].axis('off')

# Отображение канала R
axes[1].imshow(r, cmap='Reds')
axes[1].set_title('Канал R')
axes[1].axis('off')

# Отображение канала G
axes[2].imshow(g, cmap='Greens')
axes[2].set_title('Канал G')
axes[2].axis('off')

# Отображение канала B
axes[3].imshow(b, cmap='Blues')
axes[3].set_title('Канал B')
axes[3].axis('off')

# Показ всех изображений
plt.tight_layout()
plt.show()
