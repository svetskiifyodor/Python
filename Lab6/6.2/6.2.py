import xml.etree.ElementTree as ET

def update_xml(xml_file, output_file):
    # Загружаем XML файл
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Находим элементы Detail и Summary
    detail = root.find('Detail')
    summary = root.find('Summary')

    # Создаем новый элемент Item
    new_item = ET.Element('Item')
    artname = ET.SubElement(new_item, 'ArtName')
    artname.text = 'Сыр Чеддер'
    barcode = ET.SubElement(new_item, 'Barcode')
    barcode.text = '2000000000500'
    qnt = ET.SubElement(new_item, 'QNT')
    qnt.text = '120,0'
    qnt_pack = ET.SubElement(new_item, 'QNTPack')
    qnt_pack.text = '120,0'
    unit = ET.SubElement(new_item, 'Unit')
    unit.text = 'шт'
    sn1 = ET.SubElement(new_item, 'SN1')
    sn1.text = '00000020'
    sn2 = ET.SubElement(new_item, 'SN2')
    sn2.text = '05.12.2020'
    qnt_rows = ET.SubElement(new_item, 'QNTRows')
    qnt_rows.text = '10'

    # Добавляем новый элемент Item в Detail
    detail.append(new_item)

    # Пересчитываем значения Summary
    total_summ = 0
    total_rows = 0
    for item in detail.findall('Item'):
        total_summ += float(item.find('QNT').text.replace(',', '.'))
        total_rows += int(item.find('QNTRows').text)

    # Обновляем значения в Summary
    summary.find('Summ').text = str(round(total_summ, 2))
    summary.find('SummRows').text = str(total_rows)

    # Сохраняем обновленный XML файл
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)

# Пример использования
update_xml('ex_2.xml', 'updated_ex_2.xml')
