import random


def adivina_el_numero_computadora(x):

    print("===========================================")
    print("       ¡Bienvenido(a) al juego !           ")
    print("===========================================")
    print(f"Selecciona el numero entre el 1 y {x} para que la computadora intente adivinarlo")


    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar una prediccion
        if limite_inferior != limite_superior: 
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior #tambien puede ser el  limite superior



            #obtener una respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}.  Si es muy alta, ingresa (A). si es muy baja, ingresa (B), Si es correcto ingresa (C)").lower()

        if respuesta  == "a":
                limite_superior = prediccion - 1
        elif respuesta == "b":
                limite_inferior = prediccion + 1

    print(f"¡Siii! la computadora adivino tu número correctamente {prediccion}")

adivina_el_numero_computadora(10)
            #intrevalo inciial [1 10]
            #prediccion  6
            #Respuesta: "a" 
            #intrevalo [1,5]
 


