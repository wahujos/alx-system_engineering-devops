#!/usr/bin/python3
"""
importing the necesary modules in alphabetical order
"""

import json
import requests
import sys

if __name__ == "__main__":
    """
    This function exports data in the JSON format
    """
    user_id = sys.argv[1]
    json_file_path = f'{user_id}.json'
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f'users/{user_id}').json()
    tasks = requests.get(url + f'users/{user_id}/todos').json()
    user_data = {
            user_id: [
                {
                    "tasks": task['title'],
                    "completed": task['completed'],
                    "username": user.get('username')
                }
                for task in tasks
            ]
    }
    with open(json_file_path, mode='w') as json_file:
        json.dump(user_data, json_file)
