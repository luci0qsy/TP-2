dia_semana = int(input("Ingrese un número del 1 al 7 (1: lunes, 7: domingo): "))

if 1 <= dia_semana <= 5:
  print("Día laboral.")
elif dia_semana == 6 or dia_semana == 7:
  print("Fin de semana.")
else:
  print("Número de día inválido.")