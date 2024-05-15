import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Пользователи
cursor.execute('''
CREATE TABLE IF NOT EXISTS Пользователи (
id INT(11) NOT NULL AUTO_INCREMENT,
Фамилия VARCHAR(60) NOT NULL,
Имя VARCHAR(60) NOT NULL,
Отчество VARCHAR(60), 
Дата рождения DATE NOT NULL,
Электронная почта VARCHAR(50) NOT NULL,
Телефон СHAR(20),
Форма обучения ENUM("очная", "заочная", "очно-заочная") NOT NULL,
Статус TINYINT(1) NOT NULL DEFAULT = 1,
Пароль VARCHAR(32) NOT NULL,
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
