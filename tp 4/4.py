saldo = float(input("Ingrese el saldo actual: "))
monto_retiro = float(input("Ingrese el monto a retirar: "))

if monto_retiro <= saldo:
  saldo_restante = saldo - monto_retiro
  print(f"Retiro exitoso. Saldo restante: ${saldo_restante:.2f}")
else:
  print("Fondos insuficientes.")