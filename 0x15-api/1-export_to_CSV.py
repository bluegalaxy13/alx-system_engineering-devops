#!/usr/bin/python3
"""
Returns Todo list for a given employee id and exports data in the CSV format.
"""

import requests
from sys import argv


def main():
    """
    Main function to fetch user information and their todos,
    then export the data to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]

    # Fetch user information
    user = requests.get(url + "users/{}".format(USER_ID)).json()

    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()

    # Create the CSV file
    file_name = "{}.csv".format(USER_ID)
    with open(file_name, "w") as f:
        for item in todos:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    USER_ID, user["username"], item["completed"], item["title"]
                )
            )


if __name__ == "__main__":
    main()
