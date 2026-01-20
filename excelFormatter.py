import pandas as pd
import task_manager

def copy_to_clipboard():
    dataframe = pd.DataFrame(extract_data(), columns=["start_time", "task", "hours"])
    dataframe.to_clipboard(index=False, header=False)

def extract_data():
    data = task_manager.read_data()
    rows = []
    for item in data["tasks"]:
        task = item["task"]
        rows.append({
            "start_time": pd.to_datetime(task["start_time"], format="%H:%M.%d.%m.%y").strftime("%d/%m/%y"),
            "task": task["task"].strip(),
            "hours": task["hours"],
        })
    return rows

