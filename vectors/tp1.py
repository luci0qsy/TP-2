print("Producto Escalar y Vectorial de Vectores de 3 elementos")

V1 = [int(input(f"V1({i+1}): ")) for i in range(3)]
V2 = [int(input(f"V2({i+1}): ")) for i in range(3)]

producto_escalar = sum([V1[i] * V2[i] for i in range(3)])
print("El producto escalar es:", producto_escalar)

x = V1[1]*V2[2] - V1[2]*V2[1]
y = -(V1[0]*V2[2] - V1[2]*V2[0])
z = V1[0]*V2[1] - V1[1]*V2[0]
print(f"El producto vectorial es: {x}i {y}j {z}k")