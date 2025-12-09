print("Juego: Adivina el Significado")
input("\n❥ Presiona ENTER para continuar")
print("\nAyuda a Sabadínguez a escribir un poema para la feria de literatura")
input("❥ CONTINUAR")
print("\nSelecciona el significado correcto de los salvadoreñismos")
input("❥ CONTINUAR")

import random

puntaje = 0

salvadoreñismos = {"canillera":"piernas",
                   "amarre":"no m acuerdo",
                   "desteñirse":"morir",
                   "la de hacer versos":"cabeza",
                   "bisagras":"rodillas"}

letras = ["a", "b", "c"]

for salvadoreñismo, significado in salvadoreñismos.items():

    palabras = [salvadoreñismos.values()]
    palabras.remove(significado)
    palabras = random.sample(palabras, 2)

    opciones = [significado] + palabras
    random.shuffle(opciones)

    print(f"\n¿Qué significa la siguiente palabra?: {salvadoreñismo}")

    for letra, opcion in zip(letras, opciones):
        print(f"{letra}. {opcion}")

    respuesta = input("\nElige tu respuesta: ").lower()

    indice = letras.index(respuesta)
    eleccion = opciones[indice]

    if eleccion == significado:
        print("¡Correcto!")
        puntaje += 1
    else:
        print(f"Incorrecto. La respuesta correcta era: {significado}")

print(puntaje)
if puntaje >= 3:
    print("¡Gracias por ayudarme en mi poema para la feria de literatura!")
else:
    print("Bueno... al menos lo intentaste, ¡lo harás mejor en otra ocasión!")
