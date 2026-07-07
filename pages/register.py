import tkinter as tk
from tkinter import messagebox

from database.db import Database


db = Database()


class Register(tk.Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Create Account")
        self.geometry("500x550")