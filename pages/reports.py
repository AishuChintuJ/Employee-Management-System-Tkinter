import tkinter as tk

from tkinter import ttk, filedialog, messagebox

import csv

from database.db import Database


db = Database()



class ReportsPage(tk.Toplevel):


    def __init__(self,parent):

        super().__init__(parent)


        self.title(
            "Reports"
        )


        self.geometry(
            "1000x600"
        )


        self.configure(
            bg="#F3F4F6"
        )


        tk.Label(

            self,

            text="Reports Management",

            bg="#F3F4F6",

            font=("Segoe UI",24,"bold")

        ).pack(
            pady=20
        )



        buttons=tk.Frame(
            self,
            bg="#F3F4F6"
        )

        buttons.pack()



        tk.Button(
            buttons,
            text="Employees",
            command=lambda:self.load(
                db.fetch_employee()
            )

        ).grid(
            row=0,
            column=0,
            padx=10
        )



        tk.Button(
            buttons,
            text="Departments",
            command=lambda:self.load(
                db.fetch_department()
            )

        ).grid(
            row=0,
            column=1,
            padx=10
        )



        tk.Button(
            buttons,
            text="Attendance",
            command=lambda:self.load(
                db.fetch_attendance()
            )

        ).grid(
            row=0,
            column=2,
            padx=10
        )



        tk.Button(
            buttons,
            text="Salary",
            command=lambda:self.load(
                db.fetch_salary()
            )

        ).grid(
            row=0,
            column=3,
            padx=10
        )



        tk.Button(
            self,
            text="Export CSV",
            bg="#2563EB",
            fg="white",
            command=self.export

        ).pack(
            pady=15
        )



        self.table=ttk.Treeview(
            self
        )


        self.table.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )


        self.current=[]



    def load(self,data):


        self.current=data


        self.table.delete(
            *self.table.get_children()
        )


        if not data:

            return


        columns=list(

            range(

                len(data[0])

            )

        )


        self.table["columns"]=columns

        self.table["show"]="headings"


        for col in columns:

            self.table.heading(

                col,

                text=str(col)

            )


        for row in data:


            self.table.insert(

                "",

                "end",

                values=row

            )



    def export(self):


        if not self.current:


            messagebox.showerror(

                "Error",

                "No data"

            )

            return



        file=filedialog.asksaveasfilename(

            defaultextension=".csv"

        )


        if file:


            with open(

                file,

                "w",

                newline=""

            ) as f:


                writer=csv.writer(f)


                writer.writerows(

                    self.current

                )


            messagebox.showinfo(

                "Success",

                "Report Exported"

            )