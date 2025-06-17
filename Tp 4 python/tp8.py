hay_par = False

for i in range(5):
    n = int(input(f"Ingresá el número {i+1}: "))
    if n % 2 == 0:
        hay_par = True

if hay_par:
    print("Al menos uno es par.")
else:
    print(" No hay números pares.")
