import time
import os
import platform

def limpiar_pantalla():
    # Verifica el sistema operativo y limpia la pantalla
    if platform.system() == "Windows":
        os.system("cls")  # Para Windows
    else:
        os.system("clear")  # Para Unix/Linux/Mac

while True:
    hora = time.strftime("%H:%M:%S")
    limpiar_pantalla()  # Llama a la función para limpiar la pantalla
    print(hora)
    time.sleep(1)