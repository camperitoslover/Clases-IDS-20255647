#Vamos a crear nuestro primer set (esto es un docstring)

my_set = {}
print(type(my_set)) #Clase diccionario
#Generar una lista de valores no reptidos

#Ejemplo 1: Encuesta de colores
colores = {"rojo","verde","negro","azul","rojo","azul"}
print(type(colores))
print(len(colores))
print(colores)

#Diccionario: colecciones mutables
    #Puede tomar diferentes tipos de datos
    #Los índices se llaman claves 
    #Una clave asociada a una clave es un par "clave-valor"
    #Las claves pueden ser números o texto

#Ejemplo 1

mi_mascota = {
    "tipo":"perro",
    "nombre":"Phoenix",
    "edad":4,
    "personalidad":"cariñosa"}
#{tipo, nombre, edad, personalidad}
print(type(mi_mascota))

regi_mascota = {
    "edad":4,
    "tipo":"perro",
    "nombre":"Phoenix",
    
    "personalidad":"cariñosa"}

son_iguales = mi_mascota == regi_mascota #en los diccionarios, el orden es irrelevante

#Ejemplo 2

birthdays = {
    "Alice":"Apr 1",
    "Bob":"Dec 12",
    "Carol":"Mar 4"
}
birthdays["Carol"] = "Sep 12"
print(birthdays["Carol"])
birthdays["Pau"] = "Jul 31" #agregar al diccionario
print(birthdays)
del birthdays["Bob"] #eliminar del diccionario
print(birthdays)

#clave = key
#valor = value
#clave-valor = item

for f in birthdays.values():
    print(f)
    
for person, date in birthdays.items():
    print(f"El cumpleaños de {person} es el día {date}.")