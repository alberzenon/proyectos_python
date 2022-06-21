"""
Proyecto Básico de Python (Piedra, Papel o Tijera).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).
"""

import random

from sympy import true

def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n" ).lower()
    computadora = random.choice(['pi','pa', 'ti'])
    print(f"La computadora escogio: {computadora}")


    if usuario == computadora:
        return '¡Empate!'

    if gano_el_jugador(usuario,computadora):
        return '¡Ganaste!'
        
    return '¡Perdiste =(!'


def gano_el_jugador(jugador, oponete):
    #return True  si gana el jugador
    #piedra gana a tijera (pi > ti)
    #Tijera gana a papelñ (ti >pa)
    #papel gana  a piedra (oa < pi)
    if ((jugador == 'pi' and oponete == 'ti')
        or (jugador == 'ti' and oponete == 'pa')
        or (jugador == 'pa' and oponete == 'pi')):
        return True
    else:
        False


print(jugar())