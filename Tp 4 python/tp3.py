total = 0

while True:
    precio = float(input("Precio del producto (0 para terminar): "))
    if precio == 0:
        break
    total += precio

if total > 10000:
    total *= 0.9  # Aplica 10% de descuento
    print("🎁 ¡Descuento aplicado!")

print(f"Total a pagar: ${total:.2f}")
