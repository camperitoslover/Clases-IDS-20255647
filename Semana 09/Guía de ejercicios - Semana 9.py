#Menu principal
opciones = ["Mostrar productos",
        "Agregar producto",
        "Registrar nuevo cliente",
        "Mostrar clientes",
        "Registrar pedido",
        "Mostrar pedidos del día",
        "Mostrar categorías disponibles",
        "Salir"]

#Variables
clientes = []
productos = []
pedidos = []

#Sistema
cafe = True

while cafe:
        for numero, opcion in enumerate(opciones,start=1):
                print(f"{numero}. {opcion}")
        menu = int(input("Elija una opción: "))
        if menu == 8:
                cafe = False
        elif menu == 1:
                for pr in productos:
                        print(f"{"codigo"} - {"nombre"} - {"categoría"} - {"precio"}")
        elif menu == 2:
                codigo = f"C{len(clientes)+1:03}"
                nombre = input("Nombre del producto: ")
                categoría = input("Categoría: ")
                precio = float(input("Precio: "))
                productos.append({"codigo": codigo,
                                "nombre": nombre,
                                "categoría": categoría,
                                "precio": precio
                                })
        elif menu == 3:
                codigo = f"C{len(clientes)+1:03}"
                nombre = input("Nombre del cliente: ")
                correo = input("Correo: ")
                telefono = input("Teléfono: ")
                clientes.append({"codigo": codigo,
                                "nombre": nombre,
                                "correo": correo,
                                "telefono": telefono
                                })
        elif menu == 4:
                for c in clientes:
                        print(f"{"codigo"} - {"nombre"} - {"correo"} - {"telefono"}")