import tkinter as tk
from tkinter import ttk, messagebox

from database.db import Database


db = Database()



class SalaryPage(tk.Toplevel):


    def __init__(self,parent):

        super().__init__(parent)


        self.title(
            "Salary Management"
        )


        self.geometry(
            "1000x600"
        )


        self.configure(
            bg="#F3F4F6"
        )



        tk.Label(

            self,

            text="Salary Management",

            bg="#F3F4F6",

            font=("Segoe UI",24,"bold")

        ).pack(

            pady=20

        )



        frame=tk.Frame(

            self,

            bg="#F3F4F6"

        )


        frame.pack()



        self.entries={}



        fields=[

            "Employee ID",

            "Employee Name",

            "Basic Salary",

            "Bonus",

            "Allowance",

            "Deduction",

            "Tax"

        ]



        for i,name in enumerate(fields):


            tk.Label(

                frame,

                text=name,

                bg="#F3F4F6"

            ).grid(

                row=i,

                column=0,

                padx=10,

                pady=5

            )



            e=tk.Entry(

                frame,

                width=30

            )


            e.grid(

                row=i,

                column=1

            )


            self.entries[name]=e




        tk.Button(

            self,

            text="Calculate Salary",

            bg="#2563EB",

            fg="white",

            command=self.calculate

        ).pack(

            pady=15

        )




        self.table=ttk.Treeview(

            self,

            columns=(

                "ID",

                "EmpID",

                "Name",

                "Basic",

                "Bonus",

                "Allowance",

                "Deduction",

                "Tax",

                "Net"

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



    def calculate(self):


        try:


            basic=float(

                self.entries["Basic Salary"].get()

            )


            bonus=float(

                self.entries["Bonus"].get()

            )


            allowance=float(

                self.entries["Allowance"].get()

            )


            deduction=float(

                self.entries["Deduction"].get()

            )


            tax=float(

                self.entries["Tax"].get()

            )



            net=(

                basic

                + bonus

                + allowance

                - deduction

                - tax

            )



            db.add_salary(

                self.entries["Employee ID"].get(),

                self.entries["Employee Name"].get(),

                basic,

                bonus,

                allowance,

                deduction,

                tax,

                net

            )



            messagebox.showinfo(

                "Salary",

                f"Net Salary = ₹{net}"

            )


            self.load()



        except:


            messagebox.showerror(

                "Error",

                "Invalid salary input"

            )




    def load(self):


        self.table.delete(

            *self.table.get_children()

        )



        for row in db.fetch_salary():


            self.table.insert(

                "",

                "end",

                values=row

            )