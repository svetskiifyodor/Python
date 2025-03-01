from lxml import etree


def validate_xml(xml_file, xsd_file):
    # Загружаем схему XSD
    with open(xsd_file, 'r') as xsd:
        schema_doc = etree.parse(xsd)
        schema = etree.XMLSchema(schema_doc)

    # Загружаем XML файл
    with open(xml_file, 'r') as xml:
        xml_doc = etree.parse(xml)

    # Валидация XML файла по схеме
    if schema.validate(xml_doc):
        print(f"Файл {xml_file} валиден.")
    else:
        print(f"Файл {xml_file} не прошел валидацию. Ошибки:")
        for error in schema.error_log:
            print(error.message)


# Пример использования
validate_xml('ex_1.xml', 'schema.xsd')
