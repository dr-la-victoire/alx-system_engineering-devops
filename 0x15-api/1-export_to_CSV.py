#!/usr/bin/python3
"""This module gets the info of tasks done by employees"""
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
    csv = "{}.csv".format(emp_id)

    # exportimg to csv
    with open(csv, 'w') as csvfile:
        for res in data:
            csvfile.write(
                    '"{}", "{}", "{}", "{}"\n'.format(
                        emp_id, username, res.get(
                            'completed'), res.get('title')))
