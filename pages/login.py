import tkinter as tk
from tkinter import messagebox

from database.db import Database
from pages.register import Register


db = Database()


class Login(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Employee Management Login")
        self.geometry("500x500")
        self.configure(bg="#E5E7EB")


        # CARD

        frame = tk.Frame(
            self,
            bg="white",
            padx=50,
            pady=40
        )

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )


        tk.Label(
            frame,
            text="Employee Login",
            bg="white",
            fg="#2563EB",
            font=("Segoe UI",24,"bold")
        ).pack(pady=20)



        # Email

        tk.Label(
            frame,
            text="Email",
            bg="white"
        ).pack(anchor="w")


        self.email = tk.Entry(
            frame,
            width=35,
            font=("Segoe UI",11)
        )

        self.email.pack(pady=10)



        # Password

        tk.Label(
            frame,
            text="Password",
            bg="white"
        ).pack(anchor="w")


        self.password = tk.Entry(
            frame,
            width=35,
            show="*",
            font=("Segoe UI",11)
        )

        self.password.pack(pady=10)



        tk.Button(
            frame,
            text="LOGIN",
            width=25,
            bg="#2563EB",
            fg="white",
            command=self.login
        ).pack(pady=20)



        tk.Button(
            frame,
            text="Create Account",
            bd=0,
            bg="white",
            fg="#2563EB",
            command=self.open_register
        ).pack()



    # LOGIN FUNCTION

    def login(self):

        email = self.email.get()
        password = self.password.get()


        if email == "" or password == "":

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return



        user = db.login_user(
            email,
            password
        )



        if user:


            messagebox.showinfo(
                "Success",
                "Login Successful"
            )


            # close login
            self.destroy()


            # open dashboard
            from pages.dashboard import Dashboard

            app = Dashboard()

            app.mainloop()



        else:

            messagebox.showerror(
                "Error",
                "Invalid Email or Password"
            )




    def open_register(self):

        Register(self)