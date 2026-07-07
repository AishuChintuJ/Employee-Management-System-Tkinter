import tkinter as tk

from tkinter import messagebox



class SettingsPage(tk.Toplevel):


    def __init__(self,parent):


        super().__init__(parent)


        self.title(
            "Settings"
        )


        self.geometry(
            "600x400"
        )


        self.configure(
            bg="#F3F4F6"
        )



        tk.Label(

            self,

            text="Settings",

            bg="#F3F4F6",

            font=("Segoe UI",25,"bold")

        ).pack(
            pady=30
        )



        tk.Label(

            self,

            text="Admin Profile",

            bg="#F3F4F6",

            font=("Segoe UI",15)

        ).pack(
            pady=10
        )



        tk.Label(

            self,

            text="Employee Management System v1.0",

            bg="#F3F4F6"

        ).pack()



        tk.Button(

            self,

            text="Backup Database",

            width=20,

            command=self.backup

        ).pack(
            pady=20
        )



    def backup(self):


        messagebox.showinfo(

            "Backup",

            "Database backup feature ready"

        )