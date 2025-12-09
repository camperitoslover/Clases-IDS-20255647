#1

ene = int(input())
feb = int(input())
mar = int(input())

costo_total = ene*1.25 + feb*1.38 + mar*1.14

print(f"el costo total es de {costo_total}")

#2

dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

lu = int(input())
dias[0] = lu
print(dias)

ma = int(input())
dias[1] = ma
print(dias)

mier = int(input())
dias[2] = mier
print(dias)

ju = int(input())
dias[3] = ju
print(dias)

vie = int(input())
dias[4] = vie
print(dias)

#3

frutas = ["uno","dos","tres"]

nino1 = int(input()) #El número del niño
fruta = input() #cual es su fruta favorita
frutas[nino1] = fruta
print(frutas)

nino2 = int(input()) #El número del niño
fruta = input() #cual es su fruta favorita
frutas[nino2] = fruta
print(frutas)

nino3 = int(input()) #El número del niño
fruta = input() #cual es su fruta favorita
frutas[nino3] = fruta
print(frutas)

#4 crear colección de nombres de 7 alumnos en el orden en que entraron al aula

alumnos = ["Juan","Ana","Pedro"]

orden = int(input("Orden en el que entraste (1-3): "))

print(f"El niño que entró en orden {orden} se llama {alumnos[orden-1]}")

#5 crear direcciones de correo a partir de nombre y apellido

nombre = input("nombre: ")
apellido = input("apellido: ")

print(f"{nombre.lower()}.{apellido.lower()}@ISND.com")
print(f"{nombre.lower()[0]}{apellido.lower()}@ISND.com")

#6 validar con un mensaje que el valor ingresado cumple 2 condiciones:
# 1. el valor ingresado conlleva un (1) símbolo dólar 
# 2. el valor ingresado inicia con el símbolo dolar

salario = input("ingrese su salario: ")

print(salario[0] == "$")
print(salario.count("$") == 1)

#7 se nos ha asignado una palabra encriptada, la cual sirve como contraseña. la priemra letras í es la del, hay 2 letras que no so n partd e las contraserña

contraseña = "DFGUPCCBJKAJ"
print(contraseña[::2])
