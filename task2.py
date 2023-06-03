def upload_js(x):
    try:
        with open(x) as f:
            return json.load(f)  # konwertuje .json na python
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku! Spróbuj ponownie.")
        quit()
