#Registro de clientes
import datos as dat

def crear_cliente():
    #Función que crea y valida los datos del cliente
    while True:
        dui_c = input("Ingrese el DUI del cliente con guion: ")
        existe = "No"
        for c in dat.lista_clientes:
            if c["dui"] == dui_c:
                existe = "Si"
        if len(dui_c) == 10 and existe == "No":
            break
        else:
            print("El DUI debe tener 10 caracteres y no estar registrado previamente.")
    while True:
        nombre_c = input("Ingrese el nombre del cliente: ")
        if len(nombre_c) > 1:
            break
        else:
            print("El nombre debe tener al menos 2 caracteres.")
    while True:
        apellido_c = input("Ingrese el apellido del cliente: ")
        if len(apellido_c) > 1:
            break
        else:
            print("El apellido debe tener al menos 2 caracteres.")
    
    dat.lista_clientes.append({
        "dui": dui_c,
        "nombre":nombre_c,
        "apellido":apellido_c
        })

def contratar_servicio():
    while True:
        dui_s = input("Ingrese el DUI del cliente o escriba SALIR para volver al menú: ")
        existe = "No"
        contratacion = "No"
        for c in dat.lista_clientes:
            if c["dui"] == dui_s:
                existe = "Si"
        for s in dat.lista_servicios:
            if s["dui"] == dui_s:
                contratacion = "Si"
        if dui_s.lower() == "salir":
            return
        elif existe == "No" and contratacion == "Si":
            print("El cliente no está registrado o ya ha contratado un servicio.")
        else:
            break
    while True:
        print("""
        -- Servicios Disponibles --
        WD   Desarrollo Web
        DS   Ciencia de Datos
        ML   Machine Learning Aplicado
        API  Desarrollo de APIs Empresariales
        """)
        codigo_s = input("Ingrese el código del servicio a contratar [WD/DS/ML/API]:  ")
        if codigo_s.upper() != "WD" and codigo_s != "DS" and codigo_s != "ML" and codigo_s != "API":
            print("El código ingresado no es válido.")
        else:
            break
    dat.lista_servicios.append({
        "dui": dui_s,
        "codigo": codigo_s
    })
    
def listar_clientes():
    if len(dat.lista_servicios) == 0:
        print("No hay contrataciones registradas.")
        return
    while True:
        print("""
        -- Clientes por Servicio --
        1. WD
        2. DS
        3. ML
        4. API
        5. No contratados
        """)
        eleccion = input("Ingrese el servicio que desea consultar [1-5]: ")
        if eleccion == "1":
            for s in dat.lista_servicios:
                if s["codigo"] == "WD":
                    print(s["dui"])
        elif eleccion == "2":
            for s in dat.lista_servicios:
                if s["codigo"] == "DS":
                    print(s["dui"])
        elif eleccion == "3":
            for s in dat.lista_servicios:
                if s["codigo"] == "ML":
                    print(s["dui"])
        elif eleccion == "4":
            for s in dat.lista_servicios:
                if s["codigo"] == "API":
                    print(s["dui"])