def registrar_estudiante(lista_estudiantes):
    nombre_estudiante = input("Ingrese su nombre: ") #recolección del nombre del estudiante
    numero_carnet = len(lista_estudiantes) + 1 #definición del elemento numérico del carnet a partir del orden de registro
    carnet_estudiante = f"S{numero_carnet:03d}" #elaboración del carnet
    lista_estudiantes.append({ #almacenamiento de los datos en un diccionario
        "nombre": nombre_estudiante,
        "carnet": carnet_estudiante
    })

def mostrar_estudiantes(lista_estudiantes):
    n = 0 #marcador de posición
    for e in lista_estudiantes: #bucle para mostrar todos los elementos del diccionario
        print(f"""Estudiante: {lista_estudiantes[n]["nombre"]}
              Carnet: {lista_estudiantes[n]["carnet"]}
        """)
    n+=1 #aumento de 1 por cada repetición