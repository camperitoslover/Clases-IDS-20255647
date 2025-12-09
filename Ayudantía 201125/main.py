#Este es el inicio de mi sistema

#Importamos los módulos necesarios
import modulo_funciones as fn

while True:
    print("""
    -- Menú Principal --
    1. Registrar estudiante
    2. Inscribir en curso
    3. Generar reportes
    4. Salir
    """)
    opcion = input("Elija una opción [1-4]: ")
    if opcion == "1":
        fn.registrar_estudiantes()
    elif opcion == "2":
        fn.inscribir_curso()
    elif opcion == "3":
        fn.generar_reporte()
    elif opcion == "4":
        print("Gracias, vuelve pronto.")
        break
    else:
        print("La opción no es válida.")