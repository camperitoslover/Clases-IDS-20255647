nombre = "Alvin"
print(nombre[2:5:2]) #inicio : fin + 1 : salto

palabra = "RECONOCER"
print(palabra[4:]) #vacío = default
print(palabra[::2])

#Cómo revisar si la palabra es un palíndromo
palabra2 = "ratón"
print(palabra2[::-1]) 

prueba = input("Dame una palabra: ")
print(prueba==prueba[::-1])

#número vs texto
numero = "1234"
print(len(prueba))

#Todo lo que pasa por un input por defecto se vuelve string | String: cadena de caracteres
edad = int(input())
#print(len(edad))

#Origen.dependiente - propiedades y métodos
print(palabra.lower())
print(palabra2.upper())
print(palabra2.capitalize()) 
#Paréntesis vacío: las funciones llevan el nombre y el apartado de argumentos o parámetros; 
#los métodos son funciones que aplican a objetos, pueden o no requerir parámtros