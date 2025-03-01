import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
import io

# Функция для преобразования строки в число
def convert_to_float(value):
    if isinstance(value, str):
        # Удаляем пробелы, символы "р." и заменяем запятую на точку
        value = value.replace("р.", "").replace(" ", "").replace(",", ".")
    try:
        return float(value)
    except ValueError:
        return 0.0  # В случае ошибки возвращаем 0

# Загружаем обновленный файл Excel
wb = openpyxl.load_workbook("salary_report_updated.xlsx")
ws = wb.active

# Извлекаем данные из таблицы в pandas DataFrame для удобства обработки
data = []
for row in ws.iter_rows(min_row=2, min_col=1, max_col=9, values_only=True):
    if row[0] is not None and "Итог" not in str(row[2]):
        data.append({
            "Таб.номер": row[0],
            "Фамилия": row[1],
            "Отдел": row[2],
            "Сумма по окладу, руб.": row[3],
            "Сумма по надбавками, руб.": row[4],
            "Сумма зарплаты, руб.": row[5],
            "НДФЛ, %": row[6],
            "Сумма НДФЛ, %": row[7],
            "Сумма к выдаче, руб.": row[8]
        })

df = pd.DataFrame(data)

# Преобразуем столбцы, содержащие текстовые значения с валютными знаками, в числа
df['Сумма зарплаты, руб.'] = df['Сумма зарплаты, руб.'].apply(convert_to_float)

# 1. Распределение зарплат по отделам
salary_by_department = df.groupby("Отдел")["Сумма зарплаты, руб."].sum()

# 2. Создаем круговую диаграмму
fig, ax = plt.subplots()
ax.pie(salary_by_department, labels=salary_by_department.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Сохраняем диаграмму в буфер
img_buf = io.BytesIO()
plt.savefig(img_buf, format='png')
img_buf.seek(0)

# Вставляем изображение в Excel
img = Image(img_buf)
ws.add_image(img, 'K2')  # Вставка изображения правее таблицы (начиная с K2)

# Сохраняем новый файл
wb.save("salary_report_with_chart_v2.xlsx")
