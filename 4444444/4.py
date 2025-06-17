aprobados = 0
desaprobados = 0

for i in range(1, 11):
    nota = float(input(f"Ingrese la nota del alumno {i}: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")