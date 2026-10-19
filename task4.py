
import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()

for currency in root:
    print(currency.attrib)
