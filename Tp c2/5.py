import random
import string

longitud = int(input("Longitud de la contraseña: "))
usar_letras = input("¿Incluir letras? (s/n): ").lower() == "s"
usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

caracteres = ""
if usar_letras:
    caracteres += string.ascii_letters
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

if caracteres:
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")
else:
    print("Debe seleccionar al menos un tipo de carácter.")