def registrar_libro(lista_libros):
    titulo_libro = input("Ingrese el título del libro: ") #recolección del nombre del libro
    autor_libro = input("Ingrese el autor del libro: ") #recolección del autor del libro
    numero_registro = len(lista_libros) + 1 #cálculo de la cantidad de elementos en la lista
    codigo = f"L{numero_registro:03d}" #composición del código del libro (:03d para que el número sea estrictamente de 3 dígitos)
    disponible = True #marcador de estado del libro
    if disponible == True:
        estado = "Disponible"
    else:
        estado = "Prestado"
    lista_libros.append({
        "titulo": titulo_libro,
        "autor": autor_libro,
        "codigo": codigo,
        "estado": estado
    }) #almacenamiento de libros mediante diccionario
    
def mostrar_libros(lista_libros):
    n = 0 #marcador de posición
    for l in lista_libros: #bucle para mostrar todos los libros registrados
        print(f"""Código: {lista_libros[n]["codigo"]}
            Título: {lista_libros[n]["titulo"]}
            Autor: {lista_libros[n]["autor"]}
            Estado: {lista_libros[n]["estado"]}
            """)
        n+=1 #aumento de 1 por cada repetición