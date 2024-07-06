def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    while True:
        salario = float(input("Ingrese el salario del empleado: "))
        if salario >= 0:
            break
        else:
            print("El salario no puede ser negativo. Intente de nuevo.")
    return {'nombre': nombre, 'edad': edad, 'salario': salario}

def mostrar_empleados(empleados):
    if not empleados:
        print("No hay empleados para mostrar.")
    else:
        print("\nLista de empleados:")
        for idx, empleado in enumerate(empleados):
            print(f"{idx + 1}. Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}")

def buscar_empleado(empleados, nombre):
    # Esta función busca un empleado por su nombre
    for empleado in empleados:
        if empleado['nombre'] == nombre:
            print(f"Empleado encontrado - Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}")
            return empleado
    print(f"No se encontró ningún empleado con el nombre '{nombre}'")
    return None


def editar_empleado(empleados):
    nombre_buscar = input("Ingrese el nombre del empleado que desea editar: ")
    empleado = buscar_empleado(empleados, nombre_buscar)

    if empleado:
        print(
            f"Empleado encontrado - Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}")
        opcion = input("¿Qué desea editar? (nombre/edad/salario): ").lower()

        if opcion == 'nombre':
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            empleado['nombre'] = nuevo_nombre
        elif opcion == 'edad':
            nueva_edad = int(input("Ingrese la nueva edad: "))
            empleado['edad'] = nueva_edad
        elif opcion == 'salario':
            while True:
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                if nuevo_salario >= 0:
                    empleado['salario'] = nuevo_salario
                    break
                else:
                    print("El salario no puede ser negativo. Intente de nuevo.")
        else:
            print("Opción no válida.")
    else:
        print(f"No se encontró ningún empleado con el nombre '{nombre_buscar}'")
def main():
    empleados = []

    while True:
        print("\n1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado por nombre")
        print("4. Editar empleado")
        print("5. Salir")
        opcion = input("\nIngrese una opción: ")

        if opcion == '1':
            nuevo_empleado = agregar_empleado()
            empleados.append(nuevo_empleado)
            print("Empleado agregado correctamente.")

        elif opcion == '2':
            mostrar_empleados(empleados)

        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
            empleado_encontrado = buscar_empleado(empleados, nombre_buscar)
            if empleado_encontrado:
                print(
                    f"Empleado encontrado - Nombre: {empleado_encontrado['nombre']}, Edad: {empleado_encontrado['edad']}, Salario: {empleado_encontrado['salario']}")
            else:
                print(f"No se encontró ningún empleado con el nombre '{nombre_buscar}'")

        elif opcion == '4':
            editar_empleado(empleados)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
