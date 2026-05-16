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
#valído
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
def pedir_texto(pregunta):
    while True:
        valor = input(pregunta).strip()
        if valor:
            return valor
        print("  Error: Este campo no puede estar vacío.")
def pedir_fecha(pregunta):
    while True:
        valor = input(pregunta).strip()
        if validar_fecha(valor):
            return valor
        print("  Error: Formato de fecha inválido. Use por ejemplo: 19-11-2026.")
def pedir_hora(pregunta):
    while True:
        valor = input(pregunta).strip()
        if validar_hora(valor):
            return valor
        print("  Error: Formato de hora inválido. Use por ejemplo: 19:00.")
def mostrar_cita(numero, cita):
    print(f"  {numero}. {cita['cliente']} - {cita['vehiculo']} - {cita['fecha']} a las {cita['hora']}")
citas = []

# agg citas
def agregar_cita():
    print("----------------------------------")
    print("AGREGAR NUEVA CITA")
    print("----------------------------------")

    cliente = pedir_texto("  Ingrese el nombre del cliente: ")
    vehiculo = pedir_texto("  Ingrese el modelo del vehículo: ")
    fecha = pedir_fecha("  Ingrese la fecha de la cita (dd-mm-aaaa): ")
    hora = pedir_hora("  Ingrese la hora de la cita (hh:mm): ")

    citas.append({
        "cliente": cliente,
        "vehiculo": vehiculo,
        "fecha": fecha,
        "hora": hora
    })
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
    #ordenar
    ordenadas = sorted(
        citas,
        key=lambda c: datetime.strptime(f"{c['fecha']} {c['hora']}", "%d-%m-%Y %H:%M")
    )
    for numero, cita in enumerate(ordenadas, start=1):
        mostrar_cita(numero, cita)
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
            mostrar_cita(numero, cita)
#borrar citas
def eliminar_cita(citas):
    print("----------------------------------")
    print("ELIMINAR CITA")
    print("----------------------------------")

    if len(citas) == 0:
        print("  No hay citas programadas.")
        return

    ver_citas()
    try:
        numero = int(input("  Ingrese el número de la cita que desea eliminar: ").strip())
        if 1 <= numero <= len(citas):
            cita_eliminada = citas.pop(numero - 1)
            guardar_citas(citas)
            print(f"  Cita para '{cita_eliminada['cliente']}' eliminada exitosamente.")
        else:
            print("  Número de cita no válido.")
    except ValueError:
        print("  Entrada no válida. Por favor, ingrese un número.")



#menu principal
def menu():
    while True:
        print("----------------------------------")
        print("GESTOR DE CITAS - TALLER MECÁNICO")
        print("----------------------------------")
        print("1. Agregar nueva cita")
        print("2. Ver citas programadas")
        print("3. Buscar cita")
        print("4. Eliminar cita")
        print("5. Salir")
        print("----------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_cita(citas)
        elif opcion == "4":
            eliminar_cita(citas)
        elif opcion == "5":
            print("Saliendo del gestor de citas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

#iniciar el programa
if __name__ == "__main__":
    menu()