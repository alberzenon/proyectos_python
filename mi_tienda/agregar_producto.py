import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Lista de productos a agregar
productos = [
    ("Camiseta de Algodón", 15.99, 100),
    ("Pantalones Cortos", 25.50, 50),
    ("Zapatillas Deportivas", 45.00, 30),
    ("Reloj de Pulsera", 75.00, 20),
    ("Gafas de Sol", 20.00, 40),
    ("Mochila de Viaje", 35.00, 25),
    ("Auriculares Inalámbricos", 60.00, 15),
    ("Smartphone", 299.99, 10),
    ("Laptop", 799.99, 5),
    ("Tablet", 199.99, 8),
    ("Cámara Digital", 499.99, 12),
    ("Impresora", 120.00, 7),
    ("Teclado Mecánico", 89.99, 15),
    ("Ratón Inalámbrico", 29.99, 20),
    ("Funda para Laptop", 19.99, 30),
    ("Soporte para Monitor", 49.99, 10),
    ("Altavoces Bluetooth", 39.99, 18),
    ("Cargador Solar", 25.99, 22),
    ("Kit de Herramientas", 59.99, 14),
    ("Lámpara LED", 15.00, 35),
    ("Botella de Agua Reutilizable", 12.99, 50)
]

# Insertar productos en la base de datos
for nombre, precio, cantidad in productos:
    cursor.execute('INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)', (nombre, precio, cantidad))

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Productos agregados exitosamente.")
