from docx import Document

# Открываем существующий документ
doc = Document("document_with_table.docx")

# Инициализируем словарь для хранения данных
memory_data = {}

# Перебираем все строки таблицы, чтобы найти нужные данные
table = doc.tables[0]  # Предполагаем, что таблица первая в документе

# Поиск столбца с данными для ATmega328 (предполагаем, что заголовки на первой строке)
headers = [cell.text.strip() for cell in table.rows[0].cells]

# Находим индекс столбца с ATmega328
atmega328_index = headers.index("ATmega328")

# Перебираем строки, чтобы извлечь данные для ATmega328
for row in table.rows[1:]:  # Начинаем с 1, чтобы пропустить заголовок
    # Извлекаем значения из ячеек
    row_label = row.cells[0].text.strip()

    # Пропускаем пустые строки и обрабатываем только нужные
    if row_label.startswith("Flash"):
        # Для строки Flash извлекаем полный текст, включая единицу измерения
        memory_data["Flash"] = row.cells[atmega328_index].text.strip()
    elif row_label == "SRAM" or row_label == "EEPROM":
        memory_data[row_label] = row.cells[atmega328_index].text.strip()

# Выводим данные в консоль
print(memory_data)
