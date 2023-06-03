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

def choice():  # wybór rozszerzenia
    if file_extension == ".json":
        if file_extension_new == ".xml":
            JStoXML(x, y)

    if file_extension == ".json":
        if file_extension_new == ".yml":
            JStoYML(x, y)

    if file_extension == ".xml":
        if file_extension_new == ".json":
            XMLtoJS(x, y)

    if file_extension == ".xml":
        if file_extension_new == ".yml":
            XMLtoYML(x, y)

    if file_extension == ".yml":
        if file_extension_new == ".json":
            YMLtoJS(x, y)

    if file_extension == ".yml":
        if file_extension_new == ".xml":
            YMLtoXML(x, y)


checkfile()
choice()
