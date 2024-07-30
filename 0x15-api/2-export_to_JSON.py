#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

def main():
    """
    Main function to fetch user information and their todos,
    then export the data to a JSON file.
    """
    user_id = int(argv[1])
    
    # Fetch user information
    users = get('https://jsonplaceholder.typicode.com/users').json()
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        print(f"No user found with ID {user_id}")
        return
    
    # Fetch todos for the user
    todos = get('https://jsonplaceholder.typicode.com/todos', params={"userId": user_id}).json()

    # Prepare data for JSON
    user_tasks = [{"task": todo["title"], "completed": todo["completed"], "username": user["username"]} for todo in todos]
    final_data = {user_id: user_tasks}
    
    # Write to JSON file
    file_name = f"{user_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(final_data, json_file)

if __name__ == "__main__":
    main()
