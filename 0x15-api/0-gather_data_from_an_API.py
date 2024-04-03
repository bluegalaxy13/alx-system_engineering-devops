#!/usr/bin/python3
# Write a Python script that, using this REST API, for a given
# employee ID, returns information about his/her Todo list progress.

import sys
import requests

def fetch_todo_list_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        number_of_completed_tasks = len(completed_tasks)
        employee_name = todos[0]['username']  # Assumes the first todo item's 'username' represents the employee name
        print(f"Employee {employee_name} is done with tasks ({number_of_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")
    else:
        print(f"Failed to fetch data for employee ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
    else:
        employee_id = sys.argv[1]
        fetch_todo_list_progress(employee_id)
