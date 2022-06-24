#Ejercicio 3: Obtener  la fecha y Hora actuales del systemas

import datetime


ahora = datetime.datetime.now()

print(ahora)
print(type(ahora))

#Dato formateada
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))