# 📅 Gestor de Citas — Taller Mecánico
Aplicación de consola para gestionar citas de un taller mecánico, con persistencia en JSON y validación de fechas. Segundo proyecto Python, construido como parte del aprendizaje de desarrollo freelance.

---

## ¿Qué hace este programa?

Permite llevar el registro de citas de clientes de forma sencilla desde la terminal:

- **Agregar** citas con nombre del cliente, vehículo, fecha y hora
- **Ver** todas las citas ordenadas cronológicamente (por fecha y hora)
- **Buscar** citas por nombre de cliente o modelo de vehículo
- **Eliminar** citas completadas
- **Persistencia**: los datos se guardan en `citas.json` y sobreviven al cerrar el programa

```
----------------------------------
GESTOR DE CITAS - TALLER MECÁNICO
----------------------------------
1. Agregar nueva cita
2. Ver citas programadas
3. Buscar cita
4. Eliminar cita
5. Salir
----------------------------------
```

---

## Requisitos

- Python 3.x

```bash
python3 --version
```

---

## Cómo ejecutarlo

```bash
# 1. Clona el repositorio
git clone https://github.com/floffredodev/gestor-citas.git

# 2. Entra a la carpeta
cd gestor-citas

# 3. Ejecuta el programa
python3 gestor.py
```

No requiere instalar librerías externas. Usa solo módulos de la biblioteca estándar de Python.

---

## Formato de los datos

Las citas se guardan en `citas.json` con esta estructura:

```json
[
  {
    "cliente": "Carlos Pérez",
    "vehiculo": "Toyota Corolla",
    "fecha": "10-06-2026",
    "hora": "09:00"
  }
]
```

**Formato de fecha:** `dd-mm-aaaa` (ejemplo: `19-11-2026`)  
**Formato de hora:** `HH:MM` en 24h (ejemplo: `14:30`)

---

## Estructura del proyecto

```
gestor-citas/
├── gestor.py   # Programa principal
├── citas.json        # Base de datos local (se crea automáticamente)
└── README.md
```

---

## Conceptos de Python aplicados

| Concepto | Uso en el programa |
|---|---|
| `json` + `open` + `with` | Guardar y cargar citas desde disco |
| `os.path.exists()` | Verificar si el archivo existe antes de abrirlo |
| `datetime.strptime()` | Validar formato de fecha y hora, y ordenar cronológicamente |
| Listas de diccionarios | Estructura principal de datos (`citas = [{"cliente": ...}]`) |
| Funciones (`def`) | Una función por cada operación del CRUD |
| `sorted()` + `lambda` | Ordenar citas por fecha y hora combinadas |
| Lista por comprensión | Filtrar resultados en la búsqueda |
| `try / except ValueError` | Manejo de entradas inválidas del usuario |
| `if __name__ == "__main__"` | Punto de entrada estándar del programa |

---

## Autor

**Francis** — Proyecto desarrollado de forma independiente como parte de mi aprendizaje de programación en Python.

---

## Licencia

MIT — libre de usar, modificar y compartir.
