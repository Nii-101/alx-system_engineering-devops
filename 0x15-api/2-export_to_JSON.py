#!/usr/bin/python3
"""
Exports data in the json format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_id_param = {'userId': sys.argv[1]}
    todos_response = requests.get(api_url + "todos", params=user_id_param)
    todos = todos_response.json()
    employee_response = requests.get(api_url + "users/{}".format(user_id))
    employee = employee_response.json()
    user_name = employee.get("username")

    with open("{}.json".format(user_id), "w", newline="") as file:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": user_name
            } for t in todos]}, file)
