def upload_xml(x):
    try:
        with open(x) as f:
            return xmltodict.parse(f.read())  # konwertuje .xml na python
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku! Spróbuj ponownie.")
        quit()
