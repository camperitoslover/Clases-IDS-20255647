#Estructuras de datos
    #range()
    #enumerate()
    #zip()
    
#Ejemplo 1
usuarios = ["Ana","Carlos","Luis","María","Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas = ["mango","fresa","pera","sandía","piña"]

for orden, usuario in enumerate(usuarios,start=1):
    print(f"{orden} {usuario}")

for usuario, edad in zip(usuarios, edades):
    print(f"{usuario} {edad}")
    
for usuario, edad, fruta in zip(usuarios, edades, frutas):
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}.")