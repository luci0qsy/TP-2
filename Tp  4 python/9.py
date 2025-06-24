LIMITE = 20000
total = 0

while total < LIMITE:
    compra = float(input("Ingrese el monto de la compra: "))
    if total + compra > LIMITE:
        print("Límite diario superado. No se puede realizar la compra.")
        break
    total += compra
    print(f"Total acumulado: ${total}")

print("Fin del simulador.")