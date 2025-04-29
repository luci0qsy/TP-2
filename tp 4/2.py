velocidad = int(input("Ingrese la velocidad de su vehículo (en km/h): "))
limite = 60

if velocidad <= limite:
  print("Velocidad dentro del límite permitido.")
elif 61 <= velocidad <= 80:
  print("Exceso de velocidad leve.")
else:
  print("Exceso de velocidad grave.")