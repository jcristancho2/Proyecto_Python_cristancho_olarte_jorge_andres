# Importa las librerías necesarias
import os
import json
from tabulate import tabulate

# Ruta base para los archivos JSON
RUTA_BASE = 'data/'

def crearJson(nombreArchivo: str):
    """
    Crea un archivo JSON vacío si no existe.

    Parámetros:
    nombreArchivo (str): Nombre del archivo JSON.
    """
    if not os.path.isfile(RUTA_BASE + nombreArchivo):
        with open(RUTA_BASE + nombreArchivo, 'w', encoding='utf-8') as crearArchivo:
            json.dump({}, crearArchivo, indent=4)

def leerJson(nombreArchivo: str) -> dict:
    """
    Lee y devuelve el contenido de un archivo JSON.

    Parámetros:
    nombreArchivo (str): Nombre del archivo JSON.

    Retorna:
    dict: Contenido del archivo JSON.
    """
    with open(RUTA_BASE + nombreArchivo, 'r', encoding='utf-8') as leerArchivo:
        return json.load(leerArchivo)

def actualizarJson(nombreArchivo: str, informacion: dict):
    """
    Actualiza el contenido de un archivo JSON con nueva información.

    Parámetros:
    nombreArchivo (str): Nombre del archivo JSON.
    informacion (dict): Información a guardar en el archivo JSON.
    """
    with open(RUTA_BASE + nombreArchivo, 'w+', encoding='utf-8') as actualizarArchivo:
        json.dump(informacion, actualizarArchivo, indent=4)

def mostrarJsonTabla(nombreArchivo: str) -> dict:
    """
    Muestra el contenido de un archivo JSON en forma de tabla.

    Parámetros:
    nombreArchivo (str): Nombre del archivo JSON.
    """
    with open(RUTA_BASE + nombreArchivo, "r", encoding="utf-8") as mostrarJson:
        json.load(mostrarJson)
