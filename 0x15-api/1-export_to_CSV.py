#!/usr/bin/python3
"""
Dealing with module imports and ensuring that they are organized alphabetically
"""
import csv
import requests
import sys

if __name__ == "__main__":
    """
    This is used to export data to CSV format
    csv stand for comma separated values
    """
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    res_user = requests.get(url + f"/users/{user_id}").json()
    res_task = requests.get(url + f"/users/{user_id}/todos").json()
    user_name = res_user.get('name')
    csv_file_path = f"{user_id}.csv"
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in res_task:
            task_completed_status = "True" if task['completed'] else "False"
            task_title = task['title']
            csv_writer.writerow([user_id, user_name,
                                task_completed_status, task_title])
