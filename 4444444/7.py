dias_calidos = 0
suma = 0

for i in range(7):
    temp = float(input(f"Temperatura máxima del día {i+1}: "))
    suma += temp
    if temp > 30:
        dias_calidos += 1

media = suma / 7
print(f"Media semanal: {media:.1f}°C")
print(f"Días con más de 30°C: {dias_calidos}")