#!/usr/bin/python3
"""
handling imports, import the necessary  modules
"""

import requests
import sys

if __name__ == "__main__":
    """
    module documentations, this allows this module to run fro specific places
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    res_user = requests.get(url + f'users/{employee_id}')
    res_todos = requests.get(url + f'users/{employee_id}/todos')
    if res_user.status_code == 200 and res_todos.status_code == 200:
        user = res_user.json()
        todos = res_todos.json()
        employee_name = res_user.json().get('name')
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)
        print(f"Employee {employee_name} is done with tasks"
              f"({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    else:
        print("Error occurred in fetching information")
