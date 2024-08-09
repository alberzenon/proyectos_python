from flask import Flask, render_template, redirect, url_for, flash, request
from .models import User, Auto, db

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticación
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lógica de registro
        pass
    return render_template('register.html')

@app.route('/autos', methods=['GET', 'POST'])
def autos():
    if request.method == 'POST':
        # Lógica para agregar un auto
        pass
    autos = Auto.query.all()
    return render_template('autos.html', autos=autos)
