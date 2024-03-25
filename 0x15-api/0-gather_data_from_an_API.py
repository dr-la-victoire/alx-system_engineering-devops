#!/usr/bin/python3
"""This module gets the info of tasks done by employees"""
import requests
import sys

if __name__ == "__main__":
    # getting employee ID
    emp_id = sys.argv[1]
    # getting the base URL
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    # getting employee name
    response = requests.get(url)
    name = response.json().get('name')

    # getting the tasks (total and employee)
    task_url = url + "/todos"
    response = requests.get(task_url)
    tasks = response.json()
    total_tasks = len(tasks)
    emp_tasks = 0
    completed = []

    for task in tasks:
        if task['completed']:
            emp_tasks = emp_tasks + 1
            completed.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        name, emp_tasks, total_tasks))
    for comp in completed:
        print("\t {}".format(comp))
