#En este módulo desarrollamos la lógica para el sistema

import modulo_datos as dat

def registrar_estudiantes():
    #Función que valide y registre estudiante
    while True:
        carnet_i = input("Digite el número de carnet: ")
        existe = "No"
        for e in dat.estudiantes:
            if e["carnet"] == carnet_i:
                existe = "Si"
        if len(carnet_i) >= 6 and len(carnet_i) <= 10 and existe == "No":
            break
        else:
            print("El largo del carnet debe ser mayor a 5 y menor a 11, y el carnet no debe de existir")
    while True:
        nombre_i = input("Digite el nombre del estudiante: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del nombre debe ser al menos 2.")
    while True:
        apellido_i = input("Digite el apellido del estudiante: ")
        if len(apellido_i) > 1:
            break
        else:
            print("El largo del apellido debe ser al menos 2.")
    
    dat.estudiantes.append({
        "carnet":carnet_i,
        "nombre":nombre_i,
        "apellido":apellido_i})

def inscribir_curso():
    #Función para registrar alumnos
    while True:
        carnet_c = input("Digite el número de carnet o escriba SALIR para volver al menú: ")
        if carnet_c.upper() == "SALIR":
            return
        existe = "No"
        for e in dat.estudiantes:
            if e["carnet"] == carnet_c:
                existe = "Si"
        if existe == "Si":
            break
        else:
            print("El carnet no se existe en el registro.")
    while True:
        print("-- Cursos Disponibles --")
        for co, des in dat.cursos.items():
            print(f"{co}    {des}")
        codigo_c = input("Digite el código del curso que desea inscribir: ").upper()
        codigo_existe = "No"
        for co in dat.cursos.keys():
            if co == codigo_c:
                codigo_existe = "Si"
        inscripcion = "No"
        for i in dat.inscritos:
            if i[0] == carnet_c and i[1] == codigo_c:
                inscripcion = "Si"
        if inscripcion == "No" and codigo_existe == "Si":
            break
        else:
            print("Ya se encuentra inscrito a este curso o el código es inválido.")
    
    dat.inscritos.append((carnet_c,codigo_c))

def generar_reporte():
    if len(dat.inscritos) == 0:
        print("No hay inscripciones registradas.")
        return
    else:
        while True:
            print("""
            -- Inscripciones por Curso --
            1. PY
            2. JS
            3. BD
            4. SE
            5. Estudiantes sin inscripción
            """)
            try:
                opcion = int(input("Ingrese el curso que desea consultar: "))
            except:
                print("Digite un número [1-5]")
            else:
                if opcion == 1:
                    for i in dat.inscritos:
                        if i[1] == "PY":
                            print(i[0])
                elif opcion == 2:
                    for i in dat.inscritos:
                        if i[1] == "JS":
                            print(i[0])
                elif opcion == 3:
                    for i in dat.inscritos:
                        if i[1] == "BD":
                            print(i[0])
                elif opcion == 4:
                    for i in dat.inscritos:
                        if i[1] == "SE":
                            print(i[0])
                elif opcion == 5:
                    inscrito = "No"
                    for e in dat.estudiantes:
                        for i in dat.inscritos:
                            if e["carnet"] == i[0]:
                                inscrito = True
                                break
                        if inscrito == False:
                            print(e["carnet"])