combustible = 0
CONSUMO_X_KM = 0.07

while True:
    opcion = input("¿Desea cargar (C), consumir (U) o salir (S)? ").upper()
    if opcion == "S":
        break
    elif opcion == "C":
        litros = float(input("Litros cargados: "))
        combustible += litros
    elif opcion == "U":
        litros = float(input("Litros consumidos: "))
        combustible -= litros
        if combustible < 0:
            combustible = 0
    else:
        print("Opción inválida.")

print(f"Combustible restante: {combustible:.2f} litros")
if combustible < CONSUMO_X_KM * 50:
    print("No hay suficiente combustible para recorrer 50 km.")