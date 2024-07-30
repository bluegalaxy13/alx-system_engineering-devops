"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    USER_ID = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(USER_ID))

    user = user_response.json()

    USERNAME = user.get("USERNAME")

    params = {"userId": USER_ID}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([USER_ID, USERNAME, todo.get("TASK_COMPLETED_STATUS"), todo.get("TASK_TITLE")])
