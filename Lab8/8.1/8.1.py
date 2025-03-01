import sqlite3

# Подключаемся к базе данных (если базы нет, она будет создана)
conn = sqlite3.connect('delivery.db')
cursor = conn.cursor()

# Создание таблицы Курьер
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courier (
    id INTEGER PRIMARY KEY,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    passport_number TEXT,
    birth_date TEXT,
    hire_date TEXT,
    work_start_time TEXT,
    work_end_time TEXT,
    city TEXT,
    street TEXT,
    house_number TEXT,
    apartment_number TEXT,
    phone_number TEXT
)
''')

# Создание таблицы Транспорт
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transport (
    id INTEGER PRIMARY KEY,
    car_number TEXT,
    brand TEXT,
    registration_date TEXT,
    color TEXT
)
''')

# Вставка данных в таблицу Курьер
cursor.execute('''
INSERT INTO Courier (surname, name, patronymic, passport_number, birth_date, hire_date, work_start_time, work_end_time, city, street, house_number, apartment_number, phone_number)
VALUES ('Иванов', 'Иван', 'Иванович', '1234567890', '1980-01-01', '2020-05-15', '09:00', '18:00', 'Москва', 'Тверская', '12', '34', '89031234567')
''')

cursor.execute('''
INSERT INTO Courier (surname, name, patronymic, passport_number, birth_date, hire_date, work_start_time, work_end_time, city, street, house_number, apartment_number, phone_number)
VALUES ('Петров', 'Петр', 'Петрович', '0987654321', '1985-02-02', '2021-07-20', '10:00', '19:00', 'Санкт-Петербург', 'Невский', '56', '78', '89039876543')
''')

# Вставка данных в таблицу Транспорт
cursor.execute('''
INSERT INTO Transport (car_number, brand, registration_date, color)
VALUES ('A123BC', 'Toyota', '2019-04-10', 'Красный')
''')

cursor.execute('''
INSERT INTO Transport (car_number, brand, registration_date, color)
VALUES ('B456DE', 'BMW', '2020-03-12', 'Черный')
''')

# Обновление данных в таблице Курьер
cursor.execute('''
UPDATE Courier
SET phone_number = '89039999999'
WHERE id = 1
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
