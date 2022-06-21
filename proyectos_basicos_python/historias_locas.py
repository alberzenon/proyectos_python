#Concatenar cadenas de caracteres
#supongamos que queremos crear una cadena que diga
#Aprenda a programar con _____________.


# organizacion = "freCodeCamp"
# print("Aprenda a progrmar  con " + organizacion)
# print("Aprenda a programar con {}".format(organizacion))
# print(f"Aprenda a programar con {organizacion}") #f-string


#Mad libs (Historias Locas)
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Suatntivo (plural): ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona por que me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)