def upload_yml(x):
        with open(x) as f:
            return {"root": yaml.safe_load(
                f)}  # konwertuje .yml na python, dodaje roota w pliku, ponieważ możliwy jest ValueError

