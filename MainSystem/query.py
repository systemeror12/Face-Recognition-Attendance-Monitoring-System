import pyodbc as odbc


class dbQueries:
    def __init__(self, master=None):
        self.server = "DESKTOP-DG7AK17\SQLEXPRESS"
        self.database = "seeku_database"
        self.username = ""
        self.password = ""

        self.connection_string = f"Driver={{SQL Server}};Server={self.server};Database={self.database};UID={self.username};PWD={self.password}"

        self.connection = odbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

    def login_entry(self, username, password):
        query = f"SELECT * FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False

    def register_personnel(
        self,
        personnel_number,
        personnel_firstname,
        personnel_lastname,
        personnel_middlename,
        personnel_contact_number,
        personnel_address,
        personnel_type,
    ):
        query = f"INSERT INTO tbl_personnel (personnel_no, personnel_firstname, personnel_lastname, personnel_middlename, personnel_contact_no, personnel_address, personnel_type) VALUES  (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(
            query,
            (
                personnel_number,
                personnel_firstname,
                personnel_lastname,
                personnel_middlename,
                personnel_contact_number,
                personnel_address,
                personnel_type,
            ),
        )
        self.connection.commit()
        print(f"User {personnel_firstname} has been registered successfully!")


# if db.login_entry("systemeror12", "RanOnline124"):
# print("Login successful")
# else:
# print("Invalid username or password")
