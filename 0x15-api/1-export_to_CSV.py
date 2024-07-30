#!/usr/bin/python3
"""Returns Todo list for a given employee id
and axports data in the CSV format"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]

    user = requests.get(url + f"users/{USER_ID}").json()
    todos = requests.get(url + f"todos", params={"userId": USER_ID}).json()

    file = f"{USER_ID}.csv"
    with open(file, "w") as f:
        for item in todos:
            f.write(
                f'"{USER_ID}","{user["username"]}","{item["completed"]}", "{item["title"]}"\n'
            )
