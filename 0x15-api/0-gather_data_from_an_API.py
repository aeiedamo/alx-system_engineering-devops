#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(-1)
    if not (re.fullmatch(r"\d+", sys.argv[1])):
        sys.exit(-1)
    id = int(sys.argv[1])
    req = requests.get("{}/users/{}".format(REST_API, id)).json()
    taskReq = requests.get("{}/todos".format(REST_API)).json()
    empName = req.get("name")
    tasks = list(filter(lambda x: x.get("userId") == id, taskReq))
    compTasks = list(filter(lambda x: x.get("completed"), tasks))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            empName, len(compTasks), len(tasks)
        )
    )
    if len(compTasks) > 0:
        for task in compTasks:
            print("\t {}".format(task.get("title")))
