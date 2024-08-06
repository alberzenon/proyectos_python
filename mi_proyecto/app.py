from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = request.form.get('latitude')
        lon = request.form.get('longitude')
        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                # Crear un mapa centrado en las coordenadas proporcionadas
                mapa = folium.Map(location=[lat, lon], zoom_start=15)
                folium.Marker([lat, lon]).add_to(mapa)
                # Guardar el mapa en un archivo HTML
                mapa.save('templates/mapa.html')
                return render_template('mapa.html')
            except ValueError:
                return "Por favor, ingresa coordenadas válidas."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
