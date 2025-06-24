stock_inicial = int(input("Ingrese stock inicial: "))
stock_actual = stock_inicial

while stock_actual > 0:
    venta = int(input("Cantidad vendida (0 para terminar): "))
    if venta == 0:
        break
    if venta <= stock_actual:
        stock_actual -= venta
    else:
        print("No hay suficiente stock.")

    if stock_actual <= stock_inicial * 0.1:
        print("Stock bajo: menos del 10% restante.")

print("Control finalizado.")