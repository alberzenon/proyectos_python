#Ejercicio 6: Obtener un conjunto de numeros separados por coma y crear una lista

# 2, 8 , 9, 0, 1, 8    

entrada = input("Digite varios numeros separados por coma: ")

#Imprime en cadena de caracteres
print(entrada)
print(type(entrada))

#se genera un lista con el split
numeros = entrada.split(",")
print(type(numeros))
print(numeros)