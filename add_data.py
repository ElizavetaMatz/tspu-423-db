import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def add_faculties():
    cursor.execute('''
        INSERT INTO faculties (name) VALUES 
            ("ФМФ"),
            ("ИЯМС"),
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




groups = [
    # {
    #     'group_name': '423',
    #     'faculty_name': 'ФМФ',
    # },
    # {
    #     'group_name': '413',
    #     'faculty_name': 'ФМФ',
    # },
    # {
    #     'group_name': '403',
    #     'faculty_name': 'ФМФ',
    # },
    {
        'group_name': '412',
        'faculty_name': 'ФМФ',
    },
]

def add_groups():
    for item in groups:
        faculty = get_faculty_by_name(item.get('faculty_name'))
        if not faculty:
            continue
        
        faculty = faculty[0]

        add_group(item.get('group_name'), faculty[0])
           
# faculty = get_faculty_by_name('ФМФ')

# if faculty:
#     faculty = faculty[0]

# add_group('423', faculty[0])
# print(faculty)

add_groups()

# truncate_faculties()
# add_faculties()

connection.commit()
connection.close()
