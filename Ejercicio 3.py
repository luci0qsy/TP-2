correctas=int(input("Ingrese la cantidad de respuestas correctas: "))
incorrectas=int(input("Ingrese la cantidad de respuestas incorrectas: "))
blanco=int(input("Ingrese la cantidad de respuestas en blanco: "))
print()
puntaje=(correctas*3)+(incorrectas*-1)+(blanco*0)
print("El puntaje final es: ",puntaje)