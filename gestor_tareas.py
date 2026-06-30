# gestor_tareas.py
# Sistema simple de gestión de tareas de la facultad (en memoria)

tareas = []  # Lista de diccionarios: {"materia": str, "nombre": str, "fecha": str, "completada": bool}


def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas pendientes")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")


def ver_tareas():
    """Imprime todas las tareas, indicando cuáles están pendientes."""
    if not tareas:
        print("\nNo hay tareas cargadas todavía.")
        return

    print("\n--- LISTADO DE TAREAS ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅ Completada" if tarea["completada"] else "🕒 Pendiente"
        print(f"{i}. [{tarea['materia']}] {tarea['nombre']} - Vence: {tarea['fecha']} - {estado}")


def agregar_tarea():
    """Pide los datos al usuario y agrega una nueva tarea a la lista."""
    materia = input("Materia: ").strip()
    nombre = input("Nombre de la tarea: ").strip()
    fecha = input("Fecha límite (DD/MM/AAAA): ").strip()

    # Validación básica para evitar campos vacíos
    if not materia or not nombre or not fecha:
        print("⚠️ Todos los campos son obligatorios. Tarea no agregada.")
        return

    nueva_tarea = {
        "materia": materia,
        "nombre": nombre,
        "fecha": fecha,
        "completada": False
    }
    tareas.append(nueva_tarea)
    print("✅ Tarea agregada correctamente.")


def marcar_completada():
    """Permite seleccionar una tarea por número y marcarla como completada."""
    if not tareas:
        print("\nNo hay tareas para marcar como completadas.")
        return

    ver_tareas()  # Mostramos la lista para que el usuario elija el número

    try:
        opcion = int(input("\nNúmero de la tarea a marcar como completada: "))
        # Ajustamos el índice porque la lista mostrada empieza en 1
        if 1 <= opcion <= len(tareas):
            tareas[opcion - 1]["completada"] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("⚠️ Número de tarea inválido.")
    except ValueError:
        print("⚠️ Debés ingresar un número válido.")


def main():
    """Bucle principal del programa: controla el flujo según la opción elegida."""
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break  # Sale del bucle y termina el programa
        else:
            print("⚠️ Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()