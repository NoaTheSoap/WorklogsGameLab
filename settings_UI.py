import customtkinter
import settings_manager

OPTIONS = ["Work Description", "Hours", "Date", "Week number", "Empty"]
class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Settings")
        self.geometry("720x360")

        self.grab_set()

        self.settings = settings_manager.load_settings()

        title = customtkinter.CTkLabel(self, text="Format", font=("Arial", 20))
        title.pack(pady=20)

        self.dropdown_frame = customtkinter.CTkFrame(self)
        self.dropdown_frame.pack(pady=20, padx=20, fill="x")

        format_label = customtkinter.CTkLabel(self.dropdown_frame, text="Spreadsheet layout", font=("Arial", 16))
        format_label.grid(row=0, column=0, columnspan=1, pady=(10, 15))

        self.dropdowns = []
        # Generate a row of dropdowns
        for i in range(4):
            dropdown = customtkinter.CTkOptionMenu(
                self.dropdown_frame,
                values=OPTIONS,
                width=150
            )
            dropdown.set(self.settings["column_order"][i])
            dropdown.grid(row=1, column=i, padx=10, pady=10)
            self.dropdowns.append(dropdown)

        # -------- Date and number separator --------
        format_frame = customtkinter.CTkFrame(self)
        format_frame.pack(pady=(10, 0), padx=20, fill="x")

        format_label = customtkinter.CTkLabel(format_frame, text="Number & Date Format", font=("Arial", 16))
        format_label.grid(row=0, column=0, columnspan=2, pady=(10, 15))

        # Date separator
        date_label = customtkinter.CTkLabel(format_frame, text="Date separator:")
        date_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.date_entry = customtkinter.CTkEntry(format_frame, width=80)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)
        self.date_entry.insert(0, self.settings["date_separator"])

        # Decimal separator
        decimal_label = customtkinter.CTkLabel(format_frame, text="Decimal separator:")
        decimal_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.decimal_entry = customtkinter.CTkEntry(format_frame, width=80)
        self.decimal_entry.grid(row=2, column=1, padx=10, pady=5)
        self.decimal_entry.insert(0, self.settings["decimal_separator"])

        #Save settings button
        save_button = customtkinter.CTkButton(self, text="Save", command=self.save_settings)
        save_button.pack(pady=20)

    def save_settings(self):
        # Save column order
        new_order = [dropdown.get() for dropdown in self.dropdowns]
        self.settings["column_order"] = new_order
        self.settings["date_separator"] = self.date_entry.get()
        self.settings["decimal_separator"] = self.decimal_entry.get()

        settings_manager.save_settings(self.settings)
        print("Saved settings")
        self.destroy()