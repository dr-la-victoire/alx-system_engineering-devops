#!/usr/bin/python3
"""This module exports all the data of all the employees to JSON"""
import json
import requests

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users"
    file_path = "todo_all_employees.json"
    response = requests.get(url)
    data = response.json()
    dict_ = {}

    for users in data:
        user_id = users.get('id')
        username = users.get('username')
        todo_url = url + "/{}/todos".format(user_id)
        response = requests.get(todo_url)
        todos = response.json()
        dict_[user_id] = []
        for todo in todos:
            dict_[user_id].append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
                })

    with open(file_path, 'w') as json_file:
        json.dump(dict_, json_file)
