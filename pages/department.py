import tkinter as tk
from tkinter import ttk, messagebox

from database.db import Database


db = Database()


class DepartmentPage(tk.Toplevel):

    def __init__(self,parent):

        super().__init__(parent)

        self.title(
            "Department Management"
        )

        self.geometry(
            "800x500"
        )

        self.configure(
            bg="#F3F4F6"
        )

        self.selected_id=None



        tk.Label(
            self,
            text="Department Management",
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



        tk.Label(
            form,
            text="Department Name",
            bg="#F3F4F6"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )


        self.department=tk.Entry(
            form,
            width=30
        )

        self.department.grid(
            row=0,
            column=1
        )



        tk.Label(
            form,
            text="Manager",
            bg="#F3F4F6"
        ).grid(
            row=1,
            column=0
        )


        self.manager=tk.Entry(
            form,
            width=30
        )

        self.manager.grid(
            row=1,
            column=1
        )


        btn=tk.Frame(
            self,
            bg="#F3F4F6"
        )

        btn.pack(
            pady=15
        )


        tk.Button(
            btn,
            text="ADD",
            width=12,
            command=self.add
        ).grid(row=0,column=0)


        tk.Button(
            btn,
            text="UPDATE",
            width=12,
            command=self.update
        ).grid(row=0,column=1)


        tk.Button(
            btn,
            text="DELETE",
            width=12,
            command=self.delete
        ).grid(row=0,column=2)



        self.table=ttk.Treeview(
            self,
            columns=(
                "ID",
                "Department",
                "Manager"
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


        self.table.bind(
            "<<TreeviewSelect>>",
            self.select
        )


        self.load()



    def load(self):

        self.table.delete(
            *self.table.get_children()
        )


        for row in db.fetch_department():

            self.table.insert(
                "",
                "end",
                values=row
            )



    def add(self):

        db.add_department(
            self.department.get(),
            self.manager.get()
        )

        self.load()



    def select(self,event):

        row=self.table.item(
            self.table.focus()
        )["values"]


        if row:

            self.selected_id=row[0]


            self.department.delete(
                0,
                tk.END
            )

            self.manager.delete(
                0,
                tk.END
            )


            self.department.insert(
                0,
                row[1]
            )

            self.manager.insert(
                0,
                row[2]
            )



    def update(self):

        if self.selected_id:

            db.update_department(

                self.selected_id,

                self.department.get(),

                self.manager.get()

            )

            self.load()



    def delete(self):

        if self.selected_id:

            db.delete_department(
                self.selected_id
            )

            self.load()