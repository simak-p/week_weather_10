import json


def saved_data(obj: dict):
    with open('data_stor.json', 'w') as f:
        json.dump(obj, f)


def load_data():
    with open('data_stor.json') as f:
        obj = json.load(f)
        return obj
