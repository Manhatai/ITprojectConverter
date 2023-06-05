def upload_js(x):
    with open(x) as f:
           return json.load(f)  # konwertuje .json na python
