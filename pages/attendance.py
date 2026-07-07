import tkinter as tk

from tkinter import ttk

from datetime import date

from database.db import Database



db=Database()



class AttendancePage(tk.Toplevel):


    def __init__(self,parent):

        super().__init__(parent)


        self.title(
            "Attendance Management"
        )

        self.geometry(
            "850x550"
        )

        self.configure(
            bg="#F3F4F6"
        )


        self.selected=None



        tk.Label(

            self,

            text="Attendance Management",

            bg="#F3F4F6",

            font=("Segoe UI",22,"bold")

        ).pack(
            pady=20
        )



        form=tk.Frame(
            self,
            bg="#F3F4F6"
        )

        form.pack()



        labels=[

            "Employee ID",

            "Employee Name"

        ]



        self.entries={}



        for i,text in enumerate(labels):

            tk.Label(

                form,

                text=text,

                bg="#F3F4F6"

            ).grid(

                row=i,

                column=0,

                padx=10,

                pady=10

            )


            entry=tk.Entry(

                form,

                width=30

            )


            entry.grid(

                row=i,

                column=1

            )


            self.entries[text]=entry



        # date


        tk.Label(

            form,

            text="Date",

            bg="#F3F4F6"

        ).grid(
            row=2,
            column=0
        )


        self.date=tk.Entry(

            form,

            width=30

        )


        self.date.insert(

            0,

            date.today()

        )


        self.date.grid(

            row=2,

            column=1

        )



        # status


        tk.Label(

            form,

            text="Status",

            bg="#F3F4F6"

        ).grid(

            row=3,

            column=0

        )


        self.status=ttk.Combobox(

            form,

            values=[

                "Present",

                "Absent",

                "Leave"

            ],

            width=27

        )

        self.status.grid(

            row=3,

            column=1

        )



        tk.Button(

            self,

            text="Mark Attendance",

            bg="#2563EB",

            fg="white",

            command=self.add

        ).pack(

            pady=15

        )



        self.table=ttk.Treeview(

            self,

            columns=(

                "ID",

                "Emp ID",

                "Name",

                "Date",

                "Status"

            ),

            show="headings"

        )



        for col in self.table["columns"]:

            self.table.heading(

                col,

                text=col

            )



        self.table.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )



        self.load()





    def load(self):

        self.table.delete(

            *self.table.get_children()

        )


        for row in db.fetch_attendance():

            self.table.insert(

                "",

                "end",

                values=row

            )





    def add(self):


        db.add_attendance(

            self.entries["Employee ID"].get(),

            self.entries["Employee Name"].get(),

            self.date.get(),

            self.status.get()

        )


        self.load()