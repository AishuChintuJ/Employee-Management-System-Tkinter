import sqlite3


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(
            "employee.db"
        )

        self.cursor = self.conn.cursor()

        self.create_tables()



    def create_tables(self):


        # USERS

        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fullname TEXT,

        email TEXT UNIQUE,

        password TEXT

        )
        """
        )


        # EMPLOYEE

        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        phone TEXT,

        department TEXT,

        position TEXT,

        salary TEXT

        )
        """
        )



        # DEPARTMENT

        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS departments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        department_name TEXT,

        manager TEXT

        )
        """
        )



        # ATTENDANCE

        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employee_id TEXT,

        employee_name TEXT,

        date TEXT,

        status TEXT

        )
        """
        )



        # SALARY

        self.cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS salary(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employee_id TEXT,

        employee_name TEXT,

        basic_salary REAL,

        bonus REAL,

        allowance REAL,

        deduction REAL,

        tax REAL,

        net_salary REAL

        )
        """
        )


        self.conn.commit()



    # ======================
    # USER
    # ======================


    def register_user(
        self,
        fullname,
        email,
        password
    ):

        self.cursor.execute(
        """
        INSERT INTO users

        VALUES(NULL,?,?,?)
        """,
        (
            fullname,
            email,
            password
        ))

        self.conn.commit()



    def login_user(
        self,
        email,
        password
    ):

        self.cursor.execute(
        """
        SELECT * FROM users

        WHERE email=? AND password=?
        """,
        (
            email,
            password
        ))

        return self.cursor.fetchone()



    # ======================
    # EMPLOYEE
    # ======================


    def add_employee(
        self,
        name,
        email,
        phone,
        department,
        position,
        salary
    ):

        self.cursor.execute(
        """
        INSERT INTO employees

        VALUES(NULL,?,?,?,?,?,?)
        """,
        (
            name,
            email,
            phone,
            department,
            position,
            salary
        ))

        self.conn.commit()



    def fetch_employee(self):

        self.cursor.execute(
            "SELECT * FROM employees"
        )

        return self.cursor.fetchall()



    def update_employee(
        self,
        emp_id,
        name,
        email,
        phone,
        department,
        position,
        salary
    ):

        self.cursor.execute(
        """
        UPDATE employees SET

        name=?,
        email=?,
        phone=?,
        department=?,
        position=?,
        salary=?

        WHERE id=?
        """,
        (
            name,
            email,
            phone,
            department,
            position,
            salary,
            emp_id
        ))

        self.conn.commit()



    def delete_employee(
        self,
        emp_id
    ):

        self.cursor.execute(
        """
        DELETE FROM employees
        WHERE id=?
        """,
        (
            emp_id,
        ))

        self.conn.commit()



    # ======================
    # DEPARTMENT
    # ======================


    def add_department(
        self,
        name,
        manager
    ):

        self.cursor.execute(
        """
        INSERT INTO departments

        VALUES(NULL,?,?)
        """,
        (
            name,
            manager
        ))

        self.conn.commit()



    def fetch_department(self):

        self.cursor.execute(
            "SELECT * FROM departments"
        )

        return self.cursor.fetchall()



    def update_department(
        self,
        id,
        name,
        manager
    ):

        self.cursor.execute(
        """
        UPDATE departments SET

        department_name=?,

        manager=?

        WHERE id=?
        """,
        (
            name,
            manager,
            id
        ))

        self.conn.commit()



    def delete_department(
        self,
        id
    ):

        self.cursor.execute(
        """
        DELETE FROM departments

        WHERE id=?
        """,
        (id,))

        self.conn.commit()



    # ======================
    # ATTENDANCE
    # ======================


    def add_attendance(
        self,
        emp_id,
        name,
        date,
        status
    ):

        self.cursor.execute(
        """
        INSERT INTO attendance

        VALUES(NULL,?,?,?,?)
        """,
        (
            emp_id,
            name,
            date,
            status
        ))

        self.conn.commit()



    def fetch_attendance(self):

        self.cursor.execute(
            "SELECT * FROM attendance"
        )

        return self.cursor.fetchall()



    # ======================
    # SALARY
    # ======================


    def add_salary(
        self,
        emp_id,
        name,
        basic,
        bonus,
        allowance,
        deduction,
        tax,
        net
    ):


        self.cursor.execute(
        """
        INSERT INTO salary

        VALUES(NULL,?,?,?,?,?,?,?,?)
        """,
        (
            emp_id,
            name,
            basic,
            bonus,
            allowance,
            deduction,
            tax,
            net
        ))

        self.conn.commit()



    def fetch_salary(self):

        self.cursor.execute(
            "SELECT * FROM salary"
        )

        return self.cursor.fetchall()