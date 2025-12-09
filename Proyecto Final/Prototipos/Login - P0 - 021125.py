#Pantalla de inicio
print("EIEN Dating Simulator ❤︎₊ ⊹")
print("El destino tiene formas curiosas de unir a las personas… ")
print("¿Podrás encontrar el amor verdadero o perderte entre las palabras?")
print(".  +     \n ˚⠀ ⣴⠟⠉⠉⠛⢦⡀⢀⣴⠛⠉⠈⠙⠻⣄\n  ⣼⠃⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠹⣦\n ⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n ⠀⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆\n  ⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃\n ⠀⠀⠀⠀⠻⢦⣄⠀⠀⠀⠀⠀⣠⡴⠛\n ⠀⠀⠀⠀⠀⠀⠉⠛⠶⣄⠶⠋    +.  *")

#Menu principal
menu_principal = True
while menu_principal:
    eleccion = int(input("\nMenú:\n1. ¿Cómo jugar?\n2. Iniciar\n3. Salir\n4. Créditos\n"))
    if eleccion == 3:
        menu_principal = False
    elif eleccion == 1:
        print("Reglas simples:\n♡ Elige sabiamente tus respuestas… o no.\n♡ A veces el amor no tiene lógica.\n♡ Presiona enter para continuar \n♡ Y recuerda: guardar es amar tu progreso.")
        volver = (input("Presiona enter para volver al menú"))
    elif eleccion == 4:
        print("Elaborado por Los Cerotes de Alvin")
        volver = (input("Presiona enter para volver al menú"))
    elif eleccion == 2:
        usuario = input("Ingresa tu nombre para comenzar: ")
        print(f"Bienvenide, {usuario}")
        print("🌸 Escuela Inferior de Economía y Negocios 🌸")
        print("El sonido de los pasos se mezcla con el murmullo de los estudiantes.")
        input()

        print("Es el inicio de un nuevo ciclo académico...")
        input()

        print("Tú eres una nueva estudiante, recién transferida.")
        print("Tu meta: sobrevivir a las clases de economía... y, quizá, encontrar algo más.")
        input()

        print("Mientras caminas por el pasillo principal, cuatro figuras llaman tu atención.")
        input()

        print("Sabadínguez (ajustándose los lentes): 'Ah... disculpa, ¿sabías que las tortugas pueden vivir más de 100 años?'")
        print("Su voz es tranquila, pero sus ojos se iluminan al hablar.")
        input()

        print("Never (sonriente): '¡Hola! Te he visto en la clase de microeconomía. ¿Qué te parece la escuela hasta ahora?'")
        print("Tiene la energía de alguien que ya planea dirigir el país algún día.")
        input()

        print("Julian Apple (cruzado de brazos): 'Supongo que eres nueva. No te preocupes, aquí todos sobreviven... más o menos.'")
        print("Su tono es rebelde, pero algo en su mirada sugiere que le gusta enseñar, aunque no lo admitiría.")
        input()

        print("Teodoro (mirando al suelo): 'E-esto... si necesitas ayuda con los ejercicios... puedo programar algo para resolverlos.'")
        print("Su timidez contrasta con su sonrisa sincera.")
        input()

        print("Tu corazón late un poco más rápido. Parece que cada uno tiene algo especial...")
        input()

        print("Cuatro caminos. Cuatro historias.")
        print("La Escuela Inferior de Economía y Negocios acaba de abrir sus puertas para ti.")
        input()

        print("¿Con quién te gustaría hablar primero?")
        print("1. Sabadínguez - el amante de las letras y las tortugas 🐢")
        print("2. Never - el líder alegre del consejo estudiantil 📊")
        print("3. Julian Apple - el rebelde genio de las matemáticas 📐")
        print("4. Teodoro - el programador oculto entre fórmulas 💻")

        opcion = input("\nEscribe el número del personaje con el que deseas iniciar: ")