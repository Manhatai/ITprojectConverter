def upload_xml(x):
        with open(x) as f:
            return xmltodict.parse(f.read())  # konwertuje .xml na python
