#23/10/2025

numeros = ["uno","Dos","tres","cuatro"]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])

#Ejemplo count en string
nombre = "Antonio"
print(nombre.lower().count("a"))

#Ejemplo count en lista
#lower aplica para una colección de caracteres (texto)
#print(numeros.lower().count("dos")) - NO se puede
nombres = ["Ana","Antonio","Ana","José"]
print(len(nombres[0]))
print(nombres.count("Ana"))
print(nombres[0].lower().count("a"))

#diccionarios, matrices, dataframes - formas ordenadas de recuperar un dato

#Contar caracteres en una lista
nombres = ["Ana","Antonio","Ana","José"]
r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)

#Cambiar elementos de una lista
nombres = ["Ana","Antonio","Paulina","José"]
print(nombres)
nombres[2] = "Pablo"
print(nombres)

#Agregar elementos a una lista
nombres.append("Hazel") #Append: agrega al final
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres)
nombres.insert(3,"Sebas") #Insert: agrega en una posición específica
nombres.insert(int(input("Indique el índice:")),"Sebas")

#Borrar elementos de una lista
nombres.remove("Sebas") #Remove: borrar un valor/elemento de una lista
print(nombres)
nombre_borrado = nombres.pop(int(input("índice a borrar: "))-1)
print(nombres)
print(nombre_borrado)
# nombres[1].pop(3) - "pop" y "remove" no aplican para texto 

#if condición: 
    #tabulación: depende de que se cumpla la condición
nota = float(input("Indique la nota: "))
if nota >= 6:
    print("Pasó")