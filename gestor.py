# Gestor de citas

#guardar data
import json
import os
from datetime import datetime

ARCHIVO = "citas.json"

#cargamos citas
def cargar_citas():
    if not os.path.exists(ARCHIVO):
        return []
    
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)
#guardamos citas
def guardar_citas(citas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(citas, f, ensure_ascii=False, indent=2)
#valido
def validar_fecha(texto):
    try:
        datetime.strptime(texto, "%d-%m-%Y")
        return True
    except ValueError:
        return False
def validar_hora(texto):
    try:
        datetime.strptime(texto, "%H:%M")
        return True
    except ValueError:
        return False

citas = []

# agg citas
def agregar_cita():
    print("----------------------------------")
    print("AGREGAR NUEVA CITA")
    print("----------------------------------")

#pedimos al user los detalles de la cita
    cliente = input("  Nombre del cliente: ").strip()
    vehiculo = input("  Modelo del vehículo: ").strip()

#valido que los campos no estén vacíos
    if not cliente or not vehiculo:
        print("  Error: Nombre del cliente y modelo del vehículo son obligatorios.")
        return
    #bucle hasta tener fecha valida
    while True:
        fecha = input("  Fecha de la cita (dd-mm-aaaa): ").strip()
        if validar_fecha(fecha):
            break
        print("  Error: Formato de fecha inválido. Use por ejemplo: 19/11/2026.")
    #bucle hasta tener hora valida
    while True:
        hora = input("  Hora de la cita (hh:mm): ").strip() 
        if validar_hora(hora):
            break
        print("  Error: Formato de hora inválido. Use por ejemplo: 14:30.")
#creo un diccionario con los detalles de la cita
    nueva_cita = {
        "cliente": cliente,
        "vehiculo": vehiculo,
        "fecha": fecha,
        "hora": hora
    }

    citas.append(nueva_cita)
    guardar_citas(citas)
    print(f"  Cita para '{cliente}' guardada exitosamente.")

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

    print("-----------------------------------")

#funcion buscar citas
def buscar_cita(citas):
    print("----------------------------------")
    print("BUSCAR CITA")
    print("----------------------------------")

    if len(citas) == 0:
        print("  No hay citas programadas.")
        return

    busqueda = input("  Ingrese el nombre del cliente o modelo del vehículo para buscar: ").strip().lower()

    resultados = [cita for cita in citas if busqueda in cita['cliente'].lower() or busqueda in cita['vehiculo'].lower()]
    if len(resultados) == 0:
        print("  No se encontraron citas que coincidan con la búsqueda.")
    else:
        print(f"  Se encontraron {len(resultados)} cita(s) que coinciden con la búsqueda:")
        for numero, cita in enumerate(resultados, start=1):
            print(f"  {numero}. {cita['cliente']} - {cita['vehiculo']} - {cita['fecha']} a las {cita['hora']}")



#menu principal
def menu():
    while True:
        print("----------------------------------")
        print("GESTOR DE CITAS - TALLER MECÁNICO")
        print("----------------------------------")
        print("1. Agregar nueva cita")
        print("2. Ver citas programadas")
        print("3. Buscar cita")
        print("4. Salir")
        print("----------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_cita(citas)
        elif opcion == "4":
            print("Saliendo del gestor de citas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

#iniciar el programa
if __name__ == "__main__":
    menu()