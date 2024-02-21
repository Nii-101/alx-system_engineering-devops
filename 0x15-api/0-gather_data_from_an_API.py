#!/usr/bin/python3
"""
Script returns TODO list progress when given emloyee ID
"""

import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_id_param = {'userId': user_id}
    todos_response = requests.get(api_url + "todos", params=user_id_param)
    todos = todos_response.json()
    employee_response = requests.get(api_url + "users/{}".format(user_id))
    employee = employee_response.json()

    completed = [todo.get("title")
                 for todo in todos
                 if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
