LIMITE = 50000  # límite presupuestado

total = 0
while True:
    gasto = float(input("Ingrese un gasto (0 para terminar): "))
    if gasto == 0:
        break
    total += gasto

print(f"Total gastado: ${total}")
if total > LIMITE:
    print("¡Has superado el límite presupuestado!")