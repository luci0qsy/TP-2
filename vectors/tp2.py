print("Invertir vector de caracteres")

n = int(input("Ingrese dimensión del vector: "))
v = [input(f"Ingrese Caracter {i+1}: ") for i in range(n)]

for i in range(n // 2):
    v[i], v[n - 1 - i] = v[n - 1 - i], v[i]

print("Vector invertido:", ''.join(v))