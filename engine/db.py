import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO sys_command VALUES (null,'command prompt', 'C:\\Users\\Semal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'github', 'https://www.github.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://www.chatgpt.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'leetcode', 'https://www.leetcode.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'gmail', 'https://www.gmail.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'linkedin', 'https://www.linkedin.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'google drive', 'https://www.drive.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'google', 'https://www.google.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'twitter', 'https://www.x.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'amazon', 'https://www.amazon.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'medium', 'https://www.medium.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'discord', 'https://www.discord.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES (null,'spotify', 'https://www.spotify.com/')"
# cursor.execute(query)
# conn.commit()

# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns_indices = [0, 1]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# conn.commit()
# conn.close()

# query = 'Aryan'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])