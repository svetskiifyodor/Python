import json

# Путь к файлу
file_path = 'ex_3.json'

# Чтение данных из исходного файла
with open(file_path, 'r') as file:
    data = json.load(file)

# Новый объект для добавления в массив invoices
new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 3,
            "price": 30.00
        },
        {
            "name": "item 5",
            "quantity": 2,
            "price": 15.00
        }
    ]
}

# Добавление нового объекта в список invoices
data['invoices'].append(new_invoice)

# Сохранение обновленных данных в файл
with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)

print("Новый объект добавлен и файл обновлен.")
