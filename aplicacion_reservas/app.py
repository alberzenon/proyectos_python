from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de servicios disponibles
servicios = [
    {"id": 1, "nombre": "Corte de cabello", "duracion": 30},
    {"id": 2, "nombre": "Manicure", "duracion": 45},
    {"id": 3, "nombre": "Pedicure", "duracion": 60}
]

# Lista para almacenar reservas
reservas = []

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', servicios=servicios)

# Ruta para hacer una reserva
@app.route('/reserva/<int:servicio_id>', methods=['GET', 'POST'])
def reserva(servicio_id):
    servicio = next((s for s in servicios if s['id'] == servicio_id), None)
    if request.method == 'POST':
        # Procesar la reserva
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']
        reserva = {
            'nombre': nombre,
            'servicio': servicio['nombre'],
            'fecha': fecha,
            'hora': hora
        }
        reservas.append(reserva)  # Almacenar la reserva
        return redirect(url_for('confirmacion'))
    return render_template('reserva.html', servicio=servicio)

# Ruta para la página de confirmación
@app.route('/confirmacion')
def confirmacion():
    return render_template('confirmacion.html')

# Ruta para ver reservas
@app.route('/reservas')
def ver_reservas():
    return render_template('reservas.html', reservas=reservas)

if __name__ == '__main__':
    app.run(debug=True)
