#Solucionario examen parcial



#Ejercicio 5

p = input()
l = input()

print(p.index(l))
print(p.count(l) > 0)
print(l in p)

#Ejercicio 6

n = float(input())
print(n == int(n))
print(type(n) is not int)

#string tiene largo, números no
#tipos de dato se comparan con "is"

#Ejercicio 7

dui = input()
c1 = len(dui) == 10
c2 = dui[8] == "-"
print(type(int(dui[-1])) is int)

#Clase de listas

#Input
CrearItem = input()

#Lists 
"""
"""
lista = [1,2,"tresito",["ene","feb","mar"]]
print(len(lista))
print(lista)
#obtener "es" de "tres"
print(lista[2][2:].upper())
#obtener a de "marzo"
print(lista[3][2][1])

#Concatenar: unir dos cosas

n = ["uno","dos","tres"]
n = n + ["cuatro","cinco","seis","siete"]
print(n)
n[2] = "trois"
print(n)