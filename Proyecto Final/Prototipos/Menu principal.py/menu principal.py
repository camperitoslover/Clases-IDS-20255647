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