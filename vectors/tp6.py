print("Ordenar vector en forma descendente")

n = int(input("Cantidad de elementos: "))
V1 = [int(input(f"Elemento {i+1}: ")) for i in range(n)]

for i in range(n):
    for j in range(n - 1):
        if V1[j] < V1[j + 1]:
            V1[j], V1[j + 1] = V1[j + 1], V1[j]

print("Ordenado:", V1)