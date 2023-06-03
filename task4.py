def upload_yml(x):
    try:
        with open(x) as f:
            return {"root": yaml.safe_load(
                f)}  # konwertuje .yml na python, dodaje roota w pliku, ponieważ możliwy jest ValueError
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku! Spróbuj ponownie.")
        quit()
