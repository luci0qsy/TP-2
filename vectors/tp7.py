print("Insertar valor en vector ordenado ascendente")

V = [int(input(f"Valor {i+1}: ")) for i in range(10)]
nuevo = int(input("Valor a insertar: "))
V.append(nuevo)

V.sort()
print("Vector actualizado:", V)