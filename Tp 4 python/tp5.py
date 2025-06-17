num = int(input("Ingresá un número: "))
primo = True

if num < 2:
    primo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            primo = False
            break

if primo:
    print("Es un número primo.")
else:
    print("No es primo.")
