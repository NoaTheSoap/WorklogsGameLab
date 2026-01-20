import time_utils
def data_base():
    base = {
        "tasks": []
    }
    return base

def task_base(start_time, task):
    task = {
        "task": {
            "start_time": start_time,
            "end_time": None,
            "task": task,
            "hours": "Ongoing",
        }
    }
    return task