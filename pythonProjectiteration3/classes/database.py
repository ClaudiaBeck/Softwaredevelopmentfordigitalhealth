import mysql.connector

# Below we connect to the SQL server.
db = mysql.connector.connect(
    user='root',
    password='Kirsebærblomst',
    host='localhost',
    port='3306',
    database='EDR'
)


def check_username_password(username, password):
    '''This function checks for an exact match of both username and password within the database. It then returns a boolean.'''
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Person WHERE Username= '{username}' AND Password ='{password}'")
    results = cursor.fetchall()
    if results:
        return True
    else:
        return False


def fetch_patientinfo(cprnumber):
    '''This function searched for a match with a cprnumber as an argument. It fetches all data from Person table that matches said cpr number. This data is declared as variables and returned'''
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Person WHERE CPRnumber= '{cprnumber}'")
    results = cursor.fetchall()
    if results:
        name = results[0][1]
        address = results[0][2]
        phone = results[0][3]
        email = results[0][4]
        cprnumber = results[0][7]
        # Above we have created 5 variables where we store the results that we fetch from the database in the right order that they have been entered in the table.
        # For example: name = results[0][1] will return the 0'th row aka the first row of the table and the 1'st column aka the Fullname attribute.
        return name, address, phone, email, cprnumber


def search_patient(cprnumber):
    '''This function looks for a matching cpr number within the Person table. It then returns a boolean.'''
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Person WHERE CPRnumber= '{cprnumber}'")
    results = cursor.fetchall()
    if results:
        return True, cprnumber
    else:
        return False