total_min = 0

for i in range(7):
    minutos = int(input(f"Minutos de ejercicio del día {i+1}: "))
    total_min += minutos

promedio = total_min / 7
print(f"Promedio diario: {promedio:.1f} minutos")

if promedio < 30:
    print("🏃 Se recomienda aumentar la actividad física.")