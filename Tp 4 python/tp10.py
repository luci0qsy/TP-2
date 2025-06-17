while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Mostrar número secreto")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("El número secreto es 42.")
    elif opcion == "3":
        print("Hasta luego 👋")
        break
    else:
        print("Opción no válida.")