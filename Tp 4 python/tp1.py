notas = []

for i in range(5):
    nota = float(input(f"Ingresá la nota del alumno {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / 5
print(f"Promedio: {promedio:.2f}")

if promedio > 7:
    print(" ¡Muy buen promedio!")