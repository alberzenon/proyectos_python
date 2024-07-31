import sqlite3

from werkzeug.security import generate_password_hash

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()


username = 'tuusuario'
password = 'tucontrasena'
hashed_password = generate_password_hash(password)

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
conn.commit()

conn.close()