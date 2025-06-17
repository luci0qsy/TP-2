niños = adolescentes = adultos = 0

while True:
    edad = int(input("Ingresá una edad (0 para terminar): "))
    if edad == 0:
        break
    if edad < 13:
        niños += 1
    elif edad <= 17:
        adolescentes += 1
    else:
        adultos += 1

print(f"Niños: {niños}, Adolescentes: {adolescentes}, Adultos: {adultos}")