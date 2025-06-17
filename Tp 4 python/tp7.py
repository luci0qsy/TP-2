positivos = []
negativos = []

for _ in range(10):
    n = float(input("Ingresá un número: "))
    if n > 0:
        positivos.append(n)
    elif n < 0:
        negativos.append(n)

if positivos:
    print(f"Promedio positivos: {sum(positivos)/len(positivos):.2f}")
else:
    print("No hubo números positivos.")

if negativos:
    print(f"Promedio negativos: {sum(negativos)/len(negativos):.2f}")
else:
    print("No hubo números negativos.")