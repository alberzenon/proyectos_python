import string
import random

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)  # seleccionar una palabra al azar de la lista

    # Si la palabra contiene un guión o un espacio,
    # seguir seleccionando una palabra al azar.
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():
    print("=====================================")
    print("  ¡Bienvenidos al juego del ahorcado!")
    print("=====================================")

    palabra = obtener_palabra_valida(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas =set()
    abecedarios = set(string.ascii_letters)

    vidas = 7

    while len(letras_por_adivinar) >0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #Mostrar el estado actual  de la palabra 
        palaba_lista =[letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostar estado del ahoracado
        print(vidas_diccionario_visual[vidas])
        #Mostar la letras separas por un espacio
        print(f"palabra: {''.join(palaba_lista)}")

        letra_usuario =input("Escoge una letra: ").upper()


    #Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras 
    #que ya se han ingreados, se añade la letra al conjunto de letras  ingresadas
        if letra_usuario in abecedarios - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)


            #Si la  letra esta en la palabra 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra. por favor escoge una letra ")
        else:
            print("\nEsta letra no es valida.")

    #El juego llega a esta linea cuando se adivinan todas las letras d elas palabras 
    #o cuando se agotan las vidas del jugador

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahoracdo! Perdiste. Lo lamento mucho. la palabra era: {palabra}")
    else:
        print(f"¿Exelente! ¡Adivinaste la palabra {palabra}!")

if __name__ == '__main__':
    ahorcado()
