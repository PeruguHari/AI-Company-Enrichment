import json

FILE_NAME = "data.json"

def save_result(data):

    try:
        with open(FILE_NAME, "r") as f:
            results = json.load(f)

    except:
        results = []

    results.append(data)

    with open(FILE_NAME, "w") as f:
        json.dump(results, f, indent=4)


def get_results():

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    except:
        return []