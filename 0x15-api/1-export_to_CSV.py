#!/usr/bin/python3
"""
Retrieves to-do list details for a specific employee ID.

This script accepts an employee ID as a command-line input,
retrieves the associated user data and to-do list from the
JSONPlaceholder API, and displays the tasks completed by the
employee.
"""
import requests
import sys


if __name__ == "__main__":
    # This is the Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # This gets the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # This gets the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # This filters completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Thisprints the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in completed]
