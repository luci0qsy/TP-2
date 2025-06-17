print("Separar pares e impares")

tamVec = int(input("Ingrese dimensión del vector: "))
Vec = [int(input(f"Elemento {i+1}: ")) for i in range(tamVec)]

pares = [x for x in Vec if x % 2 == 0]
impares = [x for x in Vec if x % 2 != 0]

print("Pares:", pares)
print("Cantidad:", len(pares))
print("Impares:", impares)
print("Cantidad:", len(impares))

if len(pares) > len(impares):
    print("El vector de pares es el más grande")
elif len(impares) > len(pares):
    print("El vector de impares es el más grande")
else:
    print("Ambos vectores tienen igual cantidad")