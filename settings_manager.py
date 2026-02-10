import os
import json

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "excel_path": "",
    "column_order": [
        "Week number",
        "Hours",
        "Date",
        "Work Description"
    ],
    "auto_copy": False,
    "theme": "dark"
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        user_settings = json.load(f)
    return user_settings
def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)