import json
from pathlib import Path
import os
import time_utils
import jsonFormat

filepath = Path.home() / "Documents" / "WorkLogs" / "Logs"
today_path = os.path.join(filepath, time_utils.get_date()+".json")

unfinished_task = False

# Creates filepath for JSON files if not existing.
# Checks if application has been used
def used_today():
    filepath.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(today_path):
        with open(today_path,"w+") as f:
            write_data(jsonFormat.data_base())




def save(task):
    data = read_data()
    #Check if there is a task existing
    if data["tasks"]:
        #Check if task is ended
        if is_task_status():
            update_task(data)
        else:
            create_task(data, task)
        print("Task Found")
    #Start first task
    else:
        create_task(data, task)
        print("Created new task")



def create_task(data, task):
    data["tasks"].append(jsonFormat.task_base(time_utils.get_time(), task))
    write_data(data)


def update_task(data):
    last_task = data["tasks"][-1]
    task = next(iter(last_task))
    last_task[task]["end_time"] = time_utils.get_time()
    last_task[task]["hours"] = time_utils.calculate_time(last_task[task]["start_time"])
    write_data(data)


def write_data(data):
    with open(today_path, "w") as f:
        f.write(json.dumps(data, indent=4))

def read_data():
    with open(today_path,"r") as f:
        data = json.loads(f.read())
        return data

def is_task_status():
    data = read_data()

    last_task = data["tasks"][-1]
    task = next(iter(last_task))

    # Task in progress
    if last_task[task]["end_time"] is None:
        return True
    # Task ended
    else:
        return False

used_today()