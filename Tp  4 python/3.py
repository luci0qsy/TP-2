total_vasos = 0
for dia in range(1, 8):
    vasos = int(input(f"Vasos de agua tomados el día {dia}: "))
    total_vasos += vasos

promedio = total_vasos / 7
print(f"Promedio diario: {promedio:.1f} vasos")
if promedio < 8:
    print("Se recomienda aumentar el consumo de agua.")