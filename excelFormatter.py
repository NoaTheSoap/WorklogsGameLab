import pandas as pd
import task_manager
import time_utils
import settings_manager



COLUMN_MAP = {
    "Week number": "week",
    "Hours": "hours",
    "Date": "start_time",
    "Work Description": "task",
    "Empty": "empty"
}

def copy_to_clipboard():
    settings = settings_manager.load_settings()
    mapped_columns = [COLUMN_MAP[col] for col in settings["column_order"]]
    dataframe = pd.DataFrame(extract_data(), columns=mapped_columns)
    dataframe.to_clipboard(index=False, header=False)

def extract_data():
    settings = settings_manager.load_settings()
    date_separator = settings["date_separator"]
    data = task_manager.read_data()
    rows = []
    for item in data["tasks"]:
        task = item["task"]
        rows.append({
            "start_time": pd.to_datetime(task["start_time"], format="%H:%M.%d.%m.%y").strftime(f"%d{date_separator}%m{date_separator}%y"),
            "task": task["task"].strip(),
            "week": time_utils.get_week(task["start_time"]),
            "hours": task["hours"],
            "empty": ""
        })
    return rows

