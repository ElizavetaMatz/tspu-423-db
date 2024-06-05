import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


def add_faculties():
    cursor.execute('''
        INSERT INTO faculties (name) VALUES 
            ("БХФ"),
            ("ИФФ"),
            ("ФМФ"),
            ("ИИЯМС"),
            ('ТЭФ')
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
    
def add_user(last_name, first_name, fathers_name, birth_date, email, phone_number, form_of_education, status, password, pk):
    cursor.execute(f'''
        INSERT INTO users (last_name, first_name, fathers_name, birth_date, email, phone_number, form_of_education, status, password, group_id) VALUES 
            ("{last_name}", "{first_name}", "{fathers_name}", "{birth_date}", "{email}", "{phone_number}", "{form_of_education}", {status}, "{password}", {pk})   
        ''')

def get_faculty_by_name(name):
    cursor.execute(f'''
        SELECT * FROM faculties WHERE name = "{name}" LIMIT 1
        ''')

    return cursor.fetchall()

def get_group_by_name(name):
    cursor.execute(f'''
        SELECT id, name FROM groups WHERE name = "{name}" LIMIT 1
        ''')

    return cursor.fetchall()

groups = [
    {
        'group_name': '111',
        'faculty_name': 'БХФ',
    },
    {
        'group_name': '222',
        'faculty_name': 'ИФФ',
    },
    {
        'group_name': '444',
        'faculty_name': 'ИИЯМС',
    },
    {
        'group_name': '555',
        'faculty_name': 'ТЭФ',
    }
]

users = [
    { 
        'last_name': 'Русина',
        'first_name': 'Катерина',
        'fathers_name': 'Андреевна',
        'birth_date': '26.12.1992',
        'email': 'KaterinaRusina425@mail.ru',
        'phone_number': '+7 (955) 226-13-71',
        'form_of_education': 'очная',
        'status': '1',
        'password': '3aTro5jmTydu',
        'group_name': '111',
    },
    {
        'last_name': 'Шашков',
        'first_name': 'Павел',
        'fathers_name': 'Олегович',
        'birth_date': '21.06.2001',
        'email': 'PanfilShashkov679@gmail.com',
        'phone_number': '+7 (943) 643-54-78',
        'form_of_education': 'очная',
        'status': '1',
        'password': 'bjU7MQno1wvk',
        'group_name': '222',
    },
    {
        'last_name': 'Лукерин',
        'first_name': 'Сергей',
        'fathers_name': 'Федорочив',
        'birth_date': '12.05.1999',
        'email': 'SofonLukerin744@yandex.ru',
        'phone_number': '+7 (989) 273-17-34',
        'form_of_education': 'заочная',
        'status': '1',
        'password': '5XhmOIX6MF3g',
        'group_name': '333',
    },
    {
        'last_name': 'Войтова',
        'first_name': 'Арина',
        'fathers_name': 'Владимировна',
        'birth_date': '19.09.2001',
        'email': 'AlinaVoytova497@mail.ru',
        'phone_number': '+7 (987) 614-62-95',
        'form_of_education': 'заочная',
        'status': '1',
        'password': 'mWBHEmPwfPFN',
        'group_name': '444',
    },
    {
        'last_name': 'Долгих',
        'first_name': 'Константин',
        'fathers_name': 'Максимович',
        'birth_date': '10.11.2002',
        'email': 'ArtemGronskiy503.@gmail.com',
        'phone_number': '+7 (954) 862-51-89',
        'form_of_education': 'очно-заочная',
        'status': '1',
        'password': 'YW8HETiZ9fwE',
        'group_name': '555',
    },
]

def add_groups():
    for item in groups:
        faculty = get_faculty_by_name(item.get('faculty_name'))
        if not faculty:
            continue
        
        faculty = faculty[0]

        add_group(item.get('group_name'), faculty[0])

def add_users():
    for item in users:
        group = get_group_by_name(item.get('group_name'))
        if not group:
            continue
        
        group = group[0]

        add_user(item.get('last_name'), item.get('first_name'), item.get('fathers_name'), item.get('birth_date'), item.get('email'), item.get('phone_number'), item.get('form_of_education'), item.get('status'), item.get('password'), group[0])

# faculty = get_faculty_by_name('ФМФ')

# if faculty:
# faculty = faculty[0]

# add_group('423', faculty[0])
# print(faculty)
add_faculties()
add_groups()
add_users()
#truncate_faculties()


connection.commit()
connection.close()
