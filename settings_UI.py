import customtkinter

OPTIONS = ["Week number", "Hours", "Date", "Work Description"]
class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Innstillinger")
        self.geometry("400x300")

        self.grab_set()

        title = customtkinter.CTkLabel(self, text="Format", font=("Arial", 20))
        title.pack(pady=20)

        self.dropdown_frame = customtkinter.CTkFrame(self)
        self.dropdown_frame.pack(pady=20, padx=20, fill="x")

        self.dropdowns = []
        # Generate a row of dropdowns
        for i in range(4):
            dropdown = customtkinter.CTkOptionMenu(
                self.dropdown_frame,
                values=OPTIONS,
                width=150
            )
            dropdown.grid(row=0, column=i, padx=10, pady=10)
            self.dropdowns.append(dropdown)

        #Save settings button
        save_button = customtkinter.CTkButton(self, text="Save", command=self.save_settings)
        save_button.pack(pady=20)

    def save_settings(self):
        path = self.path_entry.get()
        print("Lagret:", path)
        self.destroy()