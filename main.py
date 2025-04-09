while True:
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        with open("tareas.txt", "a") as archivo:
            tarea = input("Escribe una nueva tarea: ")
            archivo.write(tarea + "\n")
            print("Tarea guardada.")
    elif opcion == "2":
        print("\nTus tareas:")
        with open("tareas.txt", "r") as archivo:
            print(archivo.read())
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
