# -*- coding: utf-8 -*-
import time
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Reloj con Python y Tkinter")

# Crear una etiqueta para mostrar la hora
etiqueta_hora = tk.Label(ventana, font=("Arial", 24), bg="white")
etiqueta_hora.pack(pady=50)

# Función para actualizar la hora
def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_hora.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)  # Actualiza cada segundo

# Iniciar el reloj
actualizar_hora()
ventana.mainloop()
