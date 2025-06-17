print("Menú para operar un vector")

V = [0]*100
i = 0
n = int(input("Ingrese tamaño del vector: "))
opc = -1

while opc != 0:
    print("\n1-Añadir  2-Eliminar  3-Listar  4-Contar  5-Media y Máximo  0-Salir")
    opc = int(input("Opción: "))

    if opc == 1 and i < n:
        V[i] = int(input("Ingrese un entero: "))
        i += 1

    elif opc == 2:
        num = int(input("Ingrese número a eliminar: "))
        if num in V[:i]:
            idx = V.index(num)
            for j in range(idx, i - 1):
                V[j] = V[j + 1]
            V[i - 1] = 0
            i -= 1

    elif opc == 3:
        print("Contenido:", V[:i])

    elif opc == 4:
        num = int(input("Ingrese número a contar: "))
        print(f"Aparece {V[:i].count(num)} veces")

    elif opc == 5 and i > 0:
        print(f"Máximo: {max(V[:i])}, Media: {sum(V[:i]) / i}")

    elif opc == 0:
        print("Fin del programa")                                   