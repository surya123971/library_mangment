import json


FILE_NAME = "library_data.json"


def save_data(books, members, history):

    data = {
        "books": books,
        "members": members,
        "history": history
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_data():

    try:

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return {
            "books": {},
            "members": {},
            "history": []
        }

    except json.JSONDecodeError:

        return {
            "books": {},
            "members": {},
            "history": []
        }