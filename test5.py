def JStoYML(x, y):  # konwersja js - yml
    print("Zrozumiano. [.json to .yml]")
    print("Próba utworzenia nowego pliku...")
    data = upload_js(x)
    return_yaml(y, data)
    print("Sukces!")

def XMLtoYML(x, y):  # kownersja xml - yml
    print("Zrozumiano. [.xml to .yml]")
    print("Próba utworzenia nowego pliku...")
    data = upload_xml(x)
    return_yaml(y, data)
    print("Sukces!")

def return_yaml(x, data):
    with open(x, 'w') as f:
        yaml.dump(data, f)  # przeksztalca przekazany plik python na .yml
