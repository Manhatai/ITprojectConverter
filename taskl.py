def JStoXML(x, y):  # konwersja js - xml
    print("Zrozumiano. [.json to .xml]")
    print("Próba utworzenia nowego pliku...")
    data = upload_js(x)
    xml_data = dicttoxml(data).decode(
        'utf-8')  # przekształca dane z pythona na ciag bajtów a nastepnie na znaki dzieki utf-8
    return_xml(y, xml_data)
    print("Sukces!")

def YMLtoXML(x, y):  # konwersja yml - xml
    print("Zrozumiano. [.yml to .xml]")
    print("Próba utworzenia nowego pliku...")
    data = upload_yml(x)
    return_xml(y, data)
    print("Sukces!")

def return_xml(x, data):
    xml_data = xmltodict.unparse(data)  # przekształca przekazany plik python na .xml
    with open(x, 'w') as f:
        f.write(xml_data)
