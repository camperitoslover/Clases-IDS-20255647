numeros = [1,2,3,4]
#print(len(numeros))
palabra = "Aulas"
#print(len(palabra))
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
#Mostrar todos los elementos de una lista
for x in dias:
    print(x)
#Mostrar los caracteres de un elemento
for x in dias[2]:
    print(x)
    #Mostrar caracteres seleccionados de todos los elementos de una lista
for x in dias:
    print(x[:2])

#Bucles:
    #finitos: "for". Se necesita una colección (string, lista, tupla, diccionario)
    #infinitos:
    
for i in range(0,10,2):
    print(i)
    
personas = ["Ana","Luis","Luisa"]
for p in personas:
    for l in p:
        print(l)
        
valores = [(1, 3 ,6),
          (2, 7, 4),
          (6, 5, 9),
          (1,10,20)]

mayores = []
minimo = int(input("Digite el mínimo: "))
for v in valores:
    for valorcito in v:
        if valorcito > 6:
            mayores.append(valorcito)
print(mayores)

#While

inicio = 0
maximo = 5

while inicio < maximo:
    print("Saludo")
    inicio = inicio + 10
    
#Ejemplo 1
presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra
gasto -= compra
print(gasto)

estado = "Conectado"
while estado == "Conectado":
    print("Hola Sebas")
    estado = input("Digite su estado: ")