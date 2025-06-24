total = 0
cant_cargas = 0

while True:
    carga = float(input("Ingrese litros cargados (0 para finalizar): "))
    if carga == 0:
        break
    total += carga
    cant_cargas += 1
    if carga < 5:
        print("Carga inferior a 5 litros. Posible error o recarga mínima.")

if cant_cargas > 0:
    promedio = total / cant_cargas
    print(f"Total cargado: {total} litros")
    print(f"Promedio por carga: {promedio:.2f} litros")