#!/usr/bin/python3
"""
Export TODO info to all employees to JSON file
"""

import json
import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(api_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(api_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
