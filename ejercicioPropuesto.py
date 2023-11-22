import datetime

# Definicion de la clase Equipo que representa la informacion de un equipo.
class Equipo:
    def __init__(self, equipo_id, cargador, mouse, estado, ambiente):
        self.id = equipo_id  # ID del equipo
        self.cargador = cargador  # Estado del cargador
        self.mouse = mouse  # Estado del mouse
        self.estado = estado  # Estado actual del equipo
        self.ambiente = ambiente  # Nuevo atributo: Ambiente del equipo

# Definicion de la clase Novedad que representa la informacion de una novedad relacionada con un equipo.
class Novedad:
    def __init__(self, fecha, descripcion, equipo):
        self.fecha = fecha  # Fecha de la novedad
        self.descripcion = descripcion  # Descripcion de la novedad
        self.equipo = equipo  # Equipo relacionado con la novedad

# Listas para almacenar equipos y novedades
equipos = []  # Lista para almacenar objetos de la clase Equipo
novedades = []  # Lista para almacenar objetos de la clase Novedad

# Funcion para agregar informacion de un nuevo equipo
def agregarEquipo():
    equipo_id = input("Ingrese el ID del equipo: ")  # Solicitar al usuario el ID del equipo
    cargador = input("Ingrese el estado del cargador: ")  # Solicitar el estado del cargador

# Funcion para agregar informacion de una nueva novedad
def agregarNovedad():
    fecha = input("Ingrese la fecha de la novedad: ")  # Solicitar la fecha de la novedad
    descripcion = input("Ingrese la descripcion de la novedad: ")  # Solicitar la descripcion de la novedad
    equipo_id = input("Ingrese el ID del equipo relacionado: ")  # Solicitar el ID del equipo relacionado

    # Verificar si el equipo existe
    equipo = next((e for e in equipos if e.id == equipo_id), None)  # Buscar el equipo en la lista de equipos
    if equipo:
        novedad = Novedad(fecha, descripcion, equipo)  # Crear un objeto de la clase Novedad
        novedades.append(novedad)  # Agregar la novedad a la lista de novedades
    else:
        print("Equipo no encontrado. No se pudo agregar la novedad.")

# Funcion para buscar y mostrar informacion de un equipo
def buscarEquipo():
    equipo_id = input("Ingrese el ID del equipo a buscar: ")  # Solicitar al usuario el ID del equipo a buscar
    equipo = next((e for e in equipos if e.id == equipo_id), None)  # Buscar el equipo en la lista de equipos

    if equipo:
        print("Informacion del equipo:")  # Mostrar la informacion del equipo
        print("ID:", equipo.id)  # Mostrar el ID del equipo
        print("Cargador:", equipo.cargador)  # Mostrar el estado del cargador del equipo
        print("Mouse:", equipo.mouse)  # Mostrar el estado del mouse del equipo
        print("Estado actual:", equipo.estado)  # Mostrar el estado actual del equipo
    else:
        print("No se encontro informacion del equipo.")
