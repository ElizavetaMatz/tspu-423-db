import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def add_faculties():
    cursor.execute('''
        INSERT INTO faculties (name) VALUES
            ("ФМФ"), 
            ("ИИЯМС"), 
            ("ТЭФ")             
     ''')

def truncate_faculties():
    cursor.execute('''
        DELETE FROM faculties
    ''')

def add_group(name, pk):
    cursor.execute(f'''
        INSERT INTO groups (name, faculty_id) VALUES
            ({name}, {pk})           
         ''')
    
def get_faculty_by_name(name):
    cursor.execute(f'''
        SELECT * FROM faculties WHERE name = "{name}" LIMIT 1
    ''')

    return cursor.fetchall()

//////////////////////////////////////////////////////////////////////////////////

def add_groups():
    cursor.execute('''
        INSERT INTO groups (name) VALUES
            ("423"), 
            ("413"), 
            ("403")             
     ''')

def truncate_groups():
    cursor.execute('''
        DELETE FROM groups
    ''')

def add_user(name, pk):
    cursor.execute(f'''
        INSERT INTO users (name, group_id) VALUES
            ({name}, {pk})           
         ''')
    
def get_group_by_name(name):
    cursor.execute(f'''
        SELECT * FROM group WHERE name = "{name}" LIMIT 1
    ''')

    return cursor.fetchall()

///////////////////////////////////////////////////////////////////////

def add_first_name():
    cursor.execute('''
        INSERT INTO fist_name (name) VALUES
            ("A"), 
            ("B"), 
            ("C")             
     ''')
def add_last_name():
    cursor.execute('''
        INSERT INTO last_name (name) VALUES
            ("1"), 
            ("2"), 
            ("3")             
     ''')
def add_birth_date():
    cursor.execute('''
        INSERT INTO birth_date (name) VALUES
            ("2003"), 
            ("2004"), 
            ("2005")             
     ''')
def add_email():
    cursor.execute('''
        INSERT INTO email (name) VALUES
            ("yandex.ru"), 
            ("gmail.com"), 
            ("mail.ru")             
     ''')
def add_form_of_education():
    cursor.execute('''
        INSERT INTO form_of_education (name) VALUES
            ("очная"), 
            ("заочная"), 
            ("очно-заочная")             
     ''')
def add_password():
    cursor.execute('''
        INSERT INTO password (name) VALUES
            ("1234"), 
            ("5678"), 
            ("0000")             
     ''')
def truncate_users():
    cursor.execute('''
        DELETE FROM users
    ''')

def get_user_by_name(name):
    cursor.execute(f'''
        SELECT * FROM users WHERE name = "{name}" LIMIT 1
    ''')

    return cursor.fetchall()

connection.commit()
connection.close()
