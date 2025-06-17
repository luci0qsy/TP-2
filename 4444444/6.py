total = 0
mayor = 0
donantes = 0

while True:
    donacion = float(input("Ingrese donación (0 para terminar): "))
    if donacion == 0:
        break
    total += donacion
    donantes += 1
    if donacion > mayor:
        mayor = donacion

print(f"Total recaudado: ${total}")
print(f"Mayor donación: ${mayor}")
print(f"Cantidad de donantes: {donantes}")