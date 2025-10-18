frase = "La programación es poderosa"
p1 = "poderosa"
if p1 in frase:
    print("¡La palabra 'poderosa' está en la frase!")
p2 = "Java"
if p2 not in frase:
    print("La palabra 'Java' no se encuentra en la frase")

p3 = "hola"
print(p3*5)

texto = "banana"
print(texto.count("a"))

mensaje = "El Salvador es un gran país"
print(mensaje.index("gran")+1)