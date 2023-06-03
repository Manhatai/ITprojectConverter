def XMLtoJS(x, y):  # konwersja xml - js
    print("Zrozumiano. [.xml to .json]")
    print("Próba utworzenia nowego pliku...")
    data = upload_xml(x)
    return_json(y, data)
    print("Sukces!")

def YMLtoJS(x, y):  # konwersja yml - js
    print("Zrozumiano. [.yml to .json]")
    print("Próba utworzenia nowego pliku...")
    data = upload_yml(x)
    return_json(y, data)
    print("Sukces!")

def return_json(x, data):
    with open(x, "w") as f:
        f.write(json.dumps(data))  # przeksztalca przekazany plik python na .json
