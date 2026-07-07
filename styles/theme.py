from tkinter import ttk


BG="#F4F6F9"
PRIMARY="#2563EB"
SIDEBAR="#111827"
WHITE="#FFFFFF"


def apply_theme(root):

    root.configure(bg=BG)


    style=ttk.Style()

    style.theme_use("clam")


    style.configure(
        "Primary.TButton",
        font=("Segoe UI",11,"bold"),
        padding=8,
        background=PRIMARY,
        foreground="white"
    )


    style.configure(
        "Treeview",
        rowheight=28,
        font=("Segoe UI",10)
    )


    style.configure(
        "Treeview.Heading",
        font=("Segoe UI",10,"bold")
    )