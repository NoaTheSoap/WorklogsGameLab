import os
import json

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "column_order": [
        "Work Description",
        "Hours",
        "Date",
        "Week number",
        "empty"
    ],
    "decimal_separator": ",",
    "date_separator": ".",
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