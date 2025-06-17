print("Buscar animal y mostrar vecinos")

n = int(input("Cantidad de animales: "))
animal = [input(f"Animal {i+1}: ") for i in range(n)]

buscado = input("Animal a buscar: ")
for i in range(n):
    if animal[i] == buscado:
        print("Vecinos del animal encontrado:")
        if i > 0:
            print("Izquierda:", animal[i - 1])
        if i < n - 1:
            print("Derecha:", animal[i + 1])
        break
else:
    print("Animal no encontrado")