CLAVE_CORRECTA = "123"
intentos = 3

while intentos > 0:
    clave = input("Ingresá la contraseña: ")
    if clave == CLAVE_CORRECTA:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f" Contraseña incorrecta. Te quedan {intentos} intento(s).")

if intentos == 0:
    print("Acceso bloqueado.")