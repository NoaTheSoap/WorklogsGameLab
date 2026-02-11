import customtkinter
import task_manager
import excelFormatter
import settings_UI

app = customtkinter.CTk()
app.title("Worklogs")
app.geometry("560x300")

def button_callback():
    if textbox.get("0.0", "end").strip() == "": return
    task_manager.save(textbox.get("0.0", "end"))
    in_progress = task_manager.is_task_status()

    if in_progress:
        textbox.configure(state="disabled")
        update_worklog()

    else:
        textbox.configure(state="normal")
        textbox.delete("0.0", "end")
    button.configure(text="End Task" if in_progress else "Start Task")
    button.configure(fg_color="#cc0000" if in_progress else "green")

def button_settings():
    settings_UI.SettingsWindow(app)


def copy_button_callback():
    excelFormatter.copy_to_clipboard()
def update_worklog():
    print("updating worklog")
    rows = excelFormatter.extract_data()
    worklog.configure(state="normal")
    worklog.delete("0.0", "end")
    for row in rows:
        line = f"{row['start_time']:<10} | {row['task']:<10}\n"
        worklog.insert("end", line)
    worklog.configure(state="disabled")

# To clipboard button
copy_button = customtkinter.CTkButton(app, text="Copy", command=copy_button_callback)
copy_button.place(x=20, y=20)

# Open settings button
settings_button = customtkinter.CTkButton(app, text="⚙", command=button_settings, width=20)
settings_button.place(x=180, y=20)

textbox = customtkinter.CTkTextbox(app, width=200, height=100)
textbox.place(x=20, y=100)

button = customtkinter.CTkButton(app, fg_color="green", hover=False, text="Start Task", width=200, height=60, command=button_callback )
button.place(x=20, y=220)

worklog = customtkinter.CTkTextbox(app, width=300, height=270)
worklog.configure(state="disabled")
worklog.place(x=240, y=20)


update_worklog()
app.mainloop()

