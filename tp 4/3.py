menu = {
    1: "Hamburguesa",
    2: "Pizza",
    3: "Ensalada",
    4: "Salir"
}

print("Menú:")
for opcion, plato in menu.items():
  print(f"{opcion}. {plato}")

seleccion = int(input("Ingrese el número de la opción deseada: "))

if seleccion in menu:
  if seleccion == 4:
    print("Gracias por su visita.")
  else:
    print(f"Usted ha seleccionado: {menu[seleccion]}")
else:
  print("Opción inválida.")