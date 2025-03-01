import json

# Исходный файл с данными пользователей
raw_file = 'ex_2.json'
formatted_file = 'ex_2_formatted.json'

# Сырые данные из файла
raw_data = '[{"name":"Estel Kuhn","phoneNumber":"967.297.2078","email":"lruecker@trantow.com","address":"30629 Miller Streets\\nEast Tiannafort, NC 95541","userAgent":"Mozilla\\/5.0 (Macintosh; PPC Mac OS X 10_5_0 rv:3.0; en-US) AppleWebKit\\/531.36.3 (KHTML, like Gecko) Version\\/4.0.4 Safari\\/531.36.3","hexcolor":"#5d9334"},{"name":"Jeramie Hahn","phoneNumber":"+1 (278) 799-5053","email":"rowan12@gmail.com","address":"93636 Ryan Wall Suite 746\\nVicentachester, GA 19009-2247","userAgent":"Mozilla\\/5.0 (Windows NT 6.0; sl-SI; rv:1.9.1.20) Gecko\\/20180123 Firefox\\/36.0","hexcolor":"#86b00f"},{"name":"Susana Upton DVM","phoneNumber":"269.902.7866","email":"oleuschke@yahoo.com","address":"6523 Bechtelar Wells Suite 742\\nSouth Braxton, NV 18064","userAgent":"Opera\\/8.98 (Windows CE; sl-SI) Presto\\/2.12.175 Version\\/10.00","hexcolor":"#4f4a47"},{"name":"Mr. Salvador Torphy I","phoneNumber":"407.281.5935","email":"chasity.white@gmail.com","address":"961 Tianna Parks\\nToneymouth, IL 38513-9235","userAgent":"Mozilla\\/5.0 (Macintosh; PPC Mac OS X 10_6_8 rv:2.0) Gecko\\/20190216 Firefox\\/36.0","hexcolor":"#1a5583"}]'

# Форматирование и запись в читабельный файл
users_data = json.loads(raw_data)  # Преобразование строки в список словарей
with open(formatted_file, 'w') as file:
    json.dump(users_data, file, indent=2)

# Извлечение и вывод словаря с именами и телефонами
user_phone_dict = {user["name"]: user["phoneNumber"] for user in users_data}
print("Имена пользователей и их телефоны:")
for name, phone in user_phone_dict.items():
    print(f"{name}: {phone}")
