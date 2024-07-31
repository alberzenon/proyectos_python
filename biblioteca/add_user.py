import sqlite3
from werkzeug.security import generate_password_hash

# Conectar a la base de datos
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Datos del nuevo usuario
username = input("Ingresa el nombre de usuario: ")
password = input("Ingresa la contraseña: ")

# Hashear la contraseña
hashed_password = generate_password_hash(password)

# Insertar el nuevo usuario en la base de datos
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("Usuario agregado exitosamente.")
except sqlite3.IntegrityError:
    print("Error: El nombre de usuario ya existe.")
finally:
    # Cerrar la conexión
    conn.close()
