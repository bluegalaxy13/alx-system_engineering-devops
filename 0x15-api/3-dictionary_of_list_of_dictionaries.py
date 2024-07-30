#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ]
}

File name must be: todo_all_employees.json
"""

import json
import requests

def fetch_user_data():
    """
    Fetch user information and to do lists for all employees.

    Returns:
        dict: A dictionary with user IDs as keys and lists of task information as values.
    """
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch all users
    users = requests.get(url + "users").json()

    data_to_export = {}

    # Iterate over each user to fetch their todos
    for user in users:
        user_id = user["id"]

        # Fetch todos for the current user
        todo_response = requests.get(url + "todos", params={"userId": user_id})
        todo_list = todo_response.json()

        # Prepare the task list for the current user
        data_to_export[user_id] = [
            {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todo_list
        ]

    return data_to_export

if __name__ == "__main__":
    # Fetch data to export
    data_to_export = fetch_user_data()

    # Write data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
