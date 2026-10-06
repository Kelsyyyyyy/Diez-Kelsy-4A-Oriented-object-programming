import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self._name = name
    # abstract method forces every child class to create its own execute_action method
    # if a child forgets to do so, Python will throw an error
    @abstractmethod
    def execute_action(self):
        pass

# SUBCLASES (POLYMORPHISM)
# Todas heredan de SmartDevice y redefinen el método execute_action

class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living room smart light")
    def execute_action(self):
        return f"{self._name} Set the brightness at 100%"

class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")
    def execute_action(self):
        return f"{self._name} Set the volume at 100%"

class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("Samsung TV")
    def execute_action(self):
        return f"{self._name} Turn off in 30 min"
# GUI TEMPLATE (PolymorphicAppTemplate)

class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("OOP Lab: Polymorphism GUI Template")
        self.geometry("480x360")
        self.resizable(False, False)

        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "rabbit.ico")

        self.iconbitmap(icon_dir)
   
        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Light": SmartLight(),
            "Speaker": SmartSpeaker(),
            "TV": SmartTV(),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="SMART HOME POLYMORPHISM",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="EXECUTE ACTION",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select a device above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.execute_action()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()
