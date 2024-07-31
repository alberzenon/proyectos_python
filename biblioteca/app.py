from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
login_manager = LoginManager()
login_manager.init_app(app)

def init_db():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    # Crear tabla de libros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')

    # Insertar libros de ejemplo si la tabla está vacía
    cursor.execute('SELECT COUNT(*) FROM books')
    if cursor.fetchone()[0] == 0:
        books = [
            ('Cien años de soledad', 'Gabriel García Márquez', 1967),
            ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605),
            ('El Principito', 'Antoine de Saint-Exupéry', 1943),
            ('1984', 'George Orwell', 1949),
            ('El amor en los tiempos del cólera', 'Gabriel García Márquez', 1985),
        ]
        cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)

    conn.commit()
    conn.close()

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.login_time = None

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return User(user[0], user[1]) if user else None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            logged_user = User(user[0], user[1])
            logged_user.login_time = datetime.now()
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
            conn.commit()
            flash('Usuario registrado exitosamente. Puedes iniciar sesión ahora.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El nombre de usuario ya existe.')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    login_time = current_user.login_time.strftime("%Y-%m-%d %H:%M:%S") if current_user.login_time else None
    return render_template('home.html', username=current_user.username, login_time=login_time)

@app.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        # Agregar un nuevo libro
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        conn.commit()
        flash('Libro agregado exitosamente.')
    
    # Manejar búsqueda
    search_query = request.args.get('search')
    if search_query:
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute('SELECT * FROM books')
    
    books = cursor.fetchall()
    conn.close()
    return render_template('books.html', books=books)

@app.route('/delete_book/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    flash('Libro eliminado exitosamente.')
    return redirect(url_for('books'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
