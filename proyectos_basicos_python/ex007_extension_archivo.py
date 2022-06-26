#Ejercicio 7: Obtener la extencion de un archivo especifico porel usuario.


nombre_archivo = input("Ingrese el nombre del archivo: ")

#main.py   1 nombre_archivo 2  extension del archivo .py 


partes_nombre_archivos = nombre_archivo.split(".")

print(partes_nombre_archivos)

print(partes_nombre_archivos[-1])