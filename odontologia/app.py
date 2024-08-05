from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('citas.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicializar la base de datos
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS citas (id INTEGER PRIMARY KEY, nombre TEXT, fecha TEXT, hora TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO citas (nombre, fecha, hora) VALUES (?, ?, ?)', (nombre, fecha, hora))
        conn.commit()
        conn.close()
        
        return redirect(url_for('citas'))
    return render_template('agendar.html')

@app.route('/citas')
def citas():
    conn = get_db_connection()
    citas = conn.execute('SELECT * FROM citas').fetchall()
    conn.close()
    return render_template('citas.html', citas=citas)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM citas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('citas'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
