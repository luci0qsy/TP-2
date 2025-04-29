edad = int(input("Ingrese la edad de la persona: "))

if edad < 18:
  print("Menor de edad.")
elif 18 <= edad <= 64:
  print("Adulto.")
else:
  print("Adulto mayor.")