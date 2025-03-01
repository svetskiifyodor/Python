import xml.etree.ElementTree as ET

# Загружаем XML файл
tree = ET.parse('ex_3.xml')
root = tree.getroot()

# Ищем все элементы, которые содержат информацию о товарах
items = root.findall(".//ТаблСчФакт//СведТов")

# Извлекаем и выводим информацию о товарах
for item in items:
    # Извлекаем атрибуты товара
    name = item.attrib.get('НаимТов')
    quantity = item.attrib.get('КолТов')
    price = item.attrib.get('ЦенаТов')

    # Печатаем данные только если они существуют
    if name and quantity and price:
        print(f'Товар: "{name}", Количество: {quantity}, Цена: "{price}"')
    else:
        print("Некоторые данные отсутствуют для данного товара.")
