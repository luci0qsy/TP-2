tareas = [] 
while True:
    print("\nOrganizador de Tareas")  
    print("1. Agregar tarea")  
    print("2. Ver tareas")  
    print("3. Cambiar estado de tarea")  
    print("4. Eliminar tarea")
    print("5. Salir")  
   
    opcion = input("Seleccione una opción: ") 

    if opcion == "1":
        nombre = input("Ingrese la descripción de la tarea: ")  
        tareas.append({"descripcion": nombre, "estado": "pendiente"})  
        print("Tarea agregada.")  
    elif opcion == "2":
        print("\nListado de tareas:")  
        for i, t in enumerate(tareas): 
            print(f"{i+1}. {t['descripcion']} - Estado: {t['estado']}")  
    elif opcion == "3":
        num = int(input("Ingrese el número de la tarea a actualizar: ")) - 1
        if 0 <= num < len(tareas):  
            nuevo_estado = input("Nuevo estado (pendiente / en progreso / completada): ")  
            tareas[num]["estado"] = nuevo_estado
            print("Estado actualizado.") 
        else:
            print("Tarea inválida.")  
    elif opcion == "4":
        num = int(input("Ingrese el número de la tarea a eliminar: ")) - 1 
        if 0 <= num < len(tareas): 
            tareas.pop(num) 
            print("Tarea eliminada.")
        else:
            print("Número inválido.") 
    elif opcion == "5":
        print("Saliendo del organizador de tareas.") 
        break 
    else:
        print("Opción inválida.")
