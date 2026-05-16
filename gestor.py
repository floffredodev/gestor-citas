# Gestor de citas
citas = []

# agg citas
def agregar_cita():
    print("----------------------------------")
    print("AGREGAR NUEVA CITA")
    print("----------------------------------")

#pedimos al user los detalles de la cita
    cliente = input("  Nombre del cliente: ").strip()
    vehiculo = input("  Modelo del vehículo: ").strip()
    fecha = input("  Fecha de la cita (DD-MM-AAAA): ").strip()
    hora = input("  Hora de la cita (HH:MM): ").strip()

#valido que los campos no estén vacíos
    if not cliente or not vehiculo or not fecha or not hora:
        print("  Error: Todos los campos son obligatorios.")
        return
    
#creo un diccionario con los detalles de la cita
    nueva_cita = {
        "cliente": cliente,
        "vehiculo": vehiculo,
        "fecha": fecha,
        "hora": hora
    }

    citas.append(nueva_cita)
    print("  Cita agregada exitosamente.")

#mostrar citas
def ver_citas():
    print("----------------------------------")
    print("LISTA DE CITAS")
    print("----------------------------------")

    if len(citas) == 0:
        print("  No hay citas programadas.")
        return

    for numero, cita in enumerate(citas, start=1):
        print(f"  {numero}. {cita['cliente']} - {cita['vehiculo']} - {cita['fecha']} a las {cita['hora']}")

    print("\n" + "-" * 50)

#menu principal
def menu():
    while True:
        print("----------------------------------")
        print("\nGESTOR DE CITAS - TALLER MECÁNICO")
        print("----------------------------------")
        print("1. Agregar nueva cita")
        print("2. Ver citas programadas")
        print("3. Salir")
        print("----------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            print("Saliendo del gestor de citas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

#iniciar el programa
if __name__ == "__main__":
    menu()