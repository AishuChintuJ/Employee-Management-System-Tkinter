import tkinter as tk

from tkinter import ttk,messagebox

from database.db import Database



db=Database()



class EmployeePage(tk.Toplevel):


    def __init__(self,parent):

        super().__init__(parent)


        self.title(
            "Employee Management"
        )


        self.geometry(
            "950x600"
        )


        self.selected_id=None



        title=tk.Label(

            self,

            text="Employee Management",

            font=("Arial",22,"bold")

        )


        title.pack(
            pady=10
        )



        form=tk.Frame(self)

        form.pack()



        self.entries={}



        fields=[

            "Name",

            "Email",

            "Phone",

            "Department",

            "Position",

            "Salary"

        ]



        for i,field in enumerate(fields):


            tk.Label(

                form,

                text=field

            ).grid(

                row=i,

                column=0,

                padx=10,

                pady=5

            )



            entry=tk.Entry(

                form,

                width=30

            )


            entry.grid(

                row=i,

                column=1

            )


            self.entries[field]=entry




        btn=tk.Frame(self)

        btn.pack(
            pady=10
        )



        tk.Button(
            btn,
            text="Add",
            width=12,
            command=self.add
        ).grid(row=0,column=0)



        tk.Button(
            btn,
            text="Update",
            width=12,
            command=self.update
        ).grid(row=0,column=1)



        tk.Button(
            btn,
            text="Delete",
            width=12,
            command=self.delete
        ).grid(row=0,column=2)



        tk.Button(
            btn,
            text="Clear",
            width=12,
            command=self.clear

        ).grid(row=0,column=3)




        columns=(

            "ID",

            "Name",

            "Email",

            "Phone",

            "Department",

            "Position",

            "Salary"

        )



        self.table=ttk.Treeview(

            self,

            columns=columns,

            show="headings"

        )



        for col in columns:


            self.table.heading(

                col,

                text=col

            )


            self.table.column(

                col,

                width=120

            )



        self.table.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10

        )


        self.table.bind(

            "<<TreeviewSelect>>",

            self.select

        )



        self.load()



    def add(self):


        values=[

            e.get()

            for e in self.entries.values()

        ]



        db.add_employee(
            *values
        )


        self.load()

        self.clear()



    def load(self):


        self.table.delete(

            *self.table.get_children()

        )


        for row in db.fetch_employee():


            self.table.insert(

                "",

                "end",

                values=row

            )



    def select(self,event):


        row=self.table.item(

            self.table.focus()

        )["values"]


        if row:


            self.selected_id=row[0]


            for i,key in enumerate(self.entries):


                self.entries[key].delete(
                    0,
                    tk.END
                )


                self.entries[key].insert(

                    0,

                    row[i+1]

                )



    def update(self):


        if self.selected_id:


            values=[

                e.get()

                for e in self.entries.values()

            ]


            db.update_employee(

                self.selected_id,

                *values

            )


            self.load()

            self.clear()



    def delete(self):


        if self.selected_id:


            db.delete_employee(

                self.selected_id

            )


            self.load()

            self.clear()




    def clear(self):


        for e in self.entries.values():

            e.delete(
                0,
                tk.END
            )


        self.selected_id=None