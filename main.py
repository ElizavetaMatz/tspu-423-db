import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Пользователи
cursor.execute('''
CREATE TABLE IF NOT EXISTS Пользователи (
id INT(11) NOT NULL AUTO_INCREMENT,
second_name VARCHAR(60) NOT NULL,
name VARCHAR(60) NOT NULL,
father_name VARCHAR(60), 
birthday DATE NOT NULL,
email VARCHAR(50) NOT NULL,
mobile СHAR(20),
form_of_education ENUM("очная", "заочная", "очно-заочная") NOT NULL,
status TINYINT(1) NOT NULL DEFAULT = 1,
password VARCHAR(32) NOT NULL,
ID_группы INT(11) NOT NULL
)
''')

# Создаем таблицу Факультет
cursor.execute('''
CREATE TABLE IF NOT EXISTS Факультет (
id INT(11) NOT NULL AUTO_INCREMENT,
Название VARCHAR(100) NOT NULL
)
''')

# Создаем таблицу Группа
cursor.execute('''
CREATE TABLE IF NOT EXISTS Группа (
id INT(11) NOT NULL AUTO_INCREMENT,
Название VARCHAR(100) NOT NULL,
ID_факультета INT(11) NOT NULL 
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
