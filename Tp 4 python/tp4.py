import random

secreto = random.randint(1, 10)
intentos = 3

while intentos > 0:
    intento = int(input("Adiviná el número (1 al 10): "))
    if intento == secreto:
        print("🎯 ¡Adivinaste!")
        break
    else:
        print("❌ Incorrecto.")
    intentos -= 1

if intentos == 0:
    print(f"El número era: {secreto}")