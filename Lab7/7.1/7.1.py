import json
from jsonschema import validate, ValidationError, SchemaError

# Определение схемы для валидации JSON
schema = {
    "type": "object",
    "properties": {
        "movies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "year": {"type": "integer"},
                    "cast": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "role": {"type": "string"}
                            },
                            "required": ["name", "role"]
                        }
                    }
                },
                "required": ["title", "year", "cast"]
            }
        }
    },
    "required": ["movies"]
}

# Оригинальный корректный файл
valid_file = 'ex_1.json'
# Создаем длинный некорректный файл
invalid_data = {
    "movies": [
        {
            "title": "The Matrix",
            "year": "1999",  # Ошибка: год должен быть числом
            "cast": [
                {"name": "Keanu Reeves", "role": "Neo"},
                {"name": "Laurence Fishburne"},  # Ошибка: отсутствует ключ "role"
                {"role": "Trinity"}  # Ошибка: отсутствует ключ "name"
            ]
        },
        {
            "year": 2001,  # Ошибка: отсутствует ключ "title"
            "cast": [
                {"name": "Elijah Wood", "role": "Frodo"},
                {"name": "Ian McKellen", "role": "Gandalf"},
                {"name": "Viggo Mortensen", "role": "Aragorn", "extra": "info"}  # Ошибка: лишнее поле
            ]
        },
        {
            "title": "Inception",
            "year": 2010,
            "cast": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page"  # Ошибка: cast должен быть массивом
        }
    ]
}

# Запись некорректного JSON в файл
invalid_file = 'ex_1_invalid.json'
with open(invalid_file, 'w') as file:
    json.dump(invalid_data, file, indent=2)

# Проверка валидности корректного файла
with open(valid_file, 'r') as file:
    valid_data = json.load(file)
try:
    validate(instance=valid_data, schema=schema)
    print("Файл ex_1.json проходит валидацию.")
except (ValidationError, SchemaError) as e:
    print(f"Файл ex_1.json не прошел валидацию: {e}")

# Проверка валидности файла с ошибками
try:
    validate(instance=invalid_data, schema=schema)
    print("Файл ex_1_invalid.json проходит валидацию.")
except (ValidationError, SchemaError) as e:
    print(f"Файл ex_1_invalid.json не прошел валидацию: {e}")
