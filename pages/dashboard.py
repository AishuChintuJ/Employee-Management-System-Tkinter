import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from database.db import Database


db = Database()


class Dashboard(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(
            "Employee Management System"
        )

        self.geometry(
            "1200x700"
        )

        self.configure(
            bg="#F3F4F6"
        )


        # ==========================
        # SIDEBAR
        # ==========================

        self.sidebar = tk.Frame(
            self,
            bg="#111827",
            width=230
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )


        tk.Label(
            self.sidebar,
            text="EMS",
            bg="#111827",
            fg="white",
            font=("Segoe UI",30,"bold")
        ).pack(
            pady=30
        )


        menu_items = [

            ("🏠 Dashboard", self.home),

            ("👥 Employees", self.employee),

            ("🏢 Departments", self.department),

            ("🕒 Attendance", self.attendance),

            ("💰 Salary", self.salary),

            ("📊 Reports", self.reports),

            ("⚙ Settings", self.settings),

            ("🚪 Logout", self.logout)

        ]


        for text, command in menu_items:

            tk.Button(
                self.sidebar,
                text=text,
                command=command,
                bg="#1F2937",
                fg="white",
                width=22,
                height=2,
                bd=0,
                anchor="w",
                font=("Segoe UI",11)
            ).pack(
                pady=5
            )



        # ==========================
        # MAIN CONTENT
        # ==========================

        self.main = tk.Frame(
            self,
            bg="#F3F4F6"
        )

        self.main.pack(
            fill="both",
            expand=True
        )


        self.home()



    # ==========================
    # CLEAR PAGE
    # ==========================

    def clear(self):

        for widget in self.main.winfo_children():

            widget.destroy()



    # ==========================
    # HOME DASHBOARD
    # ==========================


    def home(self):

        self.clear()


        tk.Label(
            self.main,
            text="Dashboard",
            bg="#F3F4F6",
            fg="#111827",
            font=("Segoe UI",28,"bold")
        ).pack(
            pady=20
        )


        tk.Label(
            self.main,
            text=f"Date : {date.today()}",
            bg="#F3F4F6",
            font=("Segoe UI",12)
        ).pack()



        # CARDS

        card_frame=tk.Frame(
            self.main,
            bg="#F3F4F6"
        )

        card_frame.pack(
            pady=30
        )


        cards=[

            (
                "Employees",
                len(db.fetch_employee())
            ),

            (
                "Departments",
                len(db.fetch_department())
            ),

            (
                "Attendance",
                len(db.fetch_attendance())
            ),

            (
                "Salary Records",
                len(db.fetch_salary())
            )

        ]


        for title,value in cards:


            card=tk.Frame(
                card_frame,
                bg="white",
                width=190,
                height=120
            )


            card.pack(
                side="left",
                padx=15
            )


            card.pack_propagate(
                False
            )


            tk.Label(
                card,
                text=title,
                bg="white",
                font=("Segoe UI",13)
            ).pack(
                pady=15
            )


            tk.Label(
                card,
                text=value,
                bg="white",
                fg="#2563EB",
                font=("Segoe UI",28,"bold")
            ).pack()



        # ======================
        # RECENT EMPLOYEES
        # ======================


        tk.Label(
            self.main,
            text="Recent Employees",
            bg="#F3F4F6",
            font=("Segoe UI",18,"bold")
        ).pack(
            pady=20
        )



        table=ttk.Treeview(
            self.main,
            columns=(
                "ID",
                "Name",
                "Department",
                "Position"
            ),
            show="headings"
        )


        for col in table["columns"]:

            table.heading(
                col,
                text=col
            )

            table.column(
                col,
                width=150
            )



        table.pack(
            fill="x",
            padx=50
        )


        for emp in db.fetch_employee()[:5]:

            table.insert(
                "",
                "end",
                values=(

                    emp[0],

                    emp[1],

                    emp[4],

                    emp[5]

                )
            )



    # ==========================
    # NAVIGATION FUNCTIONS
    # ==========================


    def employee(self):

        from pages.employee import EmployeePage

        EmployeePage(self)



    def department(self):

        from pages.department import DepartmentPage

        DepartmentPage(self)



    def attendance(self):

        from pages.attendance import AttendancePage

        AttendancePage(self)



    def salary(self):

        from pages.salary import SalaryPage

        SalaryPage(self)



    def reports(self):

        from pages.reports import ReportsPage

        ReportsPage(self)



    def settings(self):

        from pages.settings import SettingsPage

        SettingsPage(self)



    # ==========================
    # LOGOUT
    # ==========================


    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )


        if answer:

            self.destroy()


            from pages.login import Login


            Login().mainloop()