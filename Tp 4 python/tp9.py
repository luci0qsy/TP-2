menores_cero = mayores_30 = 0

while True:
    temp = float(input("Ingresá temperatura (-100 para terminar): "))
    if temp == -100:
        break
    if temp < 0:
        menores_cero += 1
    elif temp >= 30:
        mayores_30 += 1

print(f"Temperaturas < 0°C: {menores_cero}")
print(f"Temperaturas ≥ 30°C: {mayores_30}")