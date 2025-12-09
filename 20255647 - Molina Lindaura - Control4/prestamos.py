def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    carnet = input("Ingrese su carnet: ") #recolección del carnet
    v1 = False #condición 1: existencia del carnet
    
    for e in lista_estudiantes:
        if e["carnet"] == carnet: #si carnet ingresado está en la lista definida, la condición se cumple
            v1 = True
            codigo = input("Ingrese el código del libro: ") #recolección del código
            v2 = False #condición 2: existencia del libro
            for l in lista_libros:
                if l["codigo"] == codigo: #si el código del libro ingresado está en la lista, la condición se cumple
                    v2 = True
                    if l["estado"] == "Disponible": #condición 3: disponibilidad
                        fecha = input("Ingrese la fecha (DD/MM/YYYY): ") #si está disponible, ingresar la fecha
                        lista_prestamos.append({"carnet": carnet, 
                                                "fecha": fecha,
                                                "codigo": codigo}) #registro de préstamo
                        l["estado"] = "Prestado"
                    else:
                        print("El libro seleccionado no está disponible")
            if codigo == False:
                print("El libro seleccionado no existe")
    if carnet == False:
        print("El carnet ingresado no existe")

def mostrar_prestamos(lista_prestamos):
    n = 0 #marcador de posición
    for p in lista_prestamos: #bucle para mostrar todos los préstamos registrados
        print(f"""Carnet: {lista_prestamos[n]["carnet"]}
              Código: {lista_prestamos[n]["codigo"]}
              Fecha: {lista_prestamos[n]["fecha"]}
        """)
    n+=1 #añadir 1 por cada repetición