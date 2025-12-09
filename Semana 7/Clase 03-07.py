nota = float(input("Indique la nota: "))

if nota == 10:
    print("E")
else:
    if nota > 7:
        print("MB")
    else:
        if nota > 5:
            print("B")
        else:
            if nota > 3:
                print("R")
            else:
                print("M")
                
#Ejericio 1
monto = float(input("Digite el monto: "))
tipo = input("Ingrese el tipo (Local/Exportación): ")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        impuesto = 0.1
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
elif tipo.lower() == "exportación":
    if monto > 500:
        impuesto = 0.14
    else:
        if monto > 200:
            impuesto = 0.12
        else:
            if monto > 50:
                impuesto = 0.1
            else:
                impuesto = 0
else:
    print("Ese tipo no es válido")
print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f} es de {monto*impuesto:,.2f}")

#Herramientas de control de flujo

#Condicionales:
    # if
    # for: iterar sobre una secuencia y ejecutar un bloque de código para cada elemento de la secuencia. Repetir un buvle cierta cantidad de veces
    # while: repito algo cierta cantidad de veces hasta que haya una condición que diga que pare.
#Iterable: Objeto capaz de devolver sus componentes 
#Iteradores: 

nombres = ["Ana","Sebas","María","Carla"]
#Encontremos a Sebas
nombre_buscar = input("Nombre a buscar: ")
for numerito in nombres:
    if numerito == nombre_buscar:
        print("Ya lo encontré")
    else:
        print("Aquí no está")