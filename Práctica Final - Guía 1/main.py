import funciones as fn
import datos as dat

while True:
    print("""
    --- MENÚ PRINCIPAL ---
    1. Crear cliente
    2. Contratar servicio
    3. Listar clientes por servicio
    4. Salir
    """)

    opcion = input("Seleccione una opción [1-4]: ")
    if opcion == "1":
        fn.crear_cliente()
    elif opcion == "2":
        fn.contratar_servicio()
    elif opcion == "3":
        fn.listar_clientes()
    elif opcion == "4":
        print("¡Gracias por utilizar nuestros servicios!")
        break
    else:
        print("Opción inválida.")