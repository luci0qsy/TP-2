print("Buscar valor en vector")

m = int(input("Cantidad de elementos: "))
valor = [int(input("Elemento: ")) for _ in range(m)]

bus = int(input("Ingrese el valor a buscar: "))
for i in range(m):
    if valor[i] == bus:
        print(f"Posición: {i+1}")
        break
else:
    print("No encontrado")