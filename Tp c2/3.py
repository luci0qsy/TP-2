tareas = []

def mostrar_tareas():
    for i, t in enumerate(tareas):
        print(f"{i+1}. {t['descripcion']} - {t['estado']}")

def agregar_tarea():
    desc = input("Descripción de la tarea: ")
    tareas.append({"descripcion": desc, "estado": "pendiente"})

def actualizar_tarea():
    mostrar_tareas()
    i = int(input("Número de tarea a actualizar: ")) - 1
    estado = input("Nuevo estado (pendiente/en progreso/completada): ")
    tareas[i]["estado"] = estado

def eliminar_tarea():
    mostrar_tareas()
    i = int(input("Número de tarea a eliminar: ")) - 1
    tareas.pop(i)

while True:
    print("\n1. Ver tareas\n2. Agregar\n3. Actualizar\n4. Eliminar\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        actualizar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")