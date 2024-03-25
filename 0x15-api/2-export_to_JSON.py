#!/usr/bin/python3
"""This module gets the info of employees and exports to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(url)

    # getting the username
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    data = response.json()

    file_name = "{}.json".format(emp_id)

    # Putting the data into a dictionary
    the_data = {emp_id: []}

    for todos in data:
        the_data[emp_id].append({
            "task": todos.get("title"),
            "completed": todos.get("completed"),
            "username": username
            })

    with open(file_name, "w") as json_file:
        json.dump(the_data, json_file)
