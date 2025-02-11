import os
import json

RUTA_BASE='data/'

def crearJson(nombreArchivo:str):
    if not os.path.isfile(RUTA_BASE+nombreArchivo):
        with open(RUTA_BASE+nombreArchivo, 'w', encoding='utf-8') as crearArchivo:
            json.dump({}, crearArchivo,indent=4)

def leerJson(nombreArchivo:str)-> dict:
    with open(RUTA_BASE+nombreArchivo, 'r', encoding='utf-8') as leerArchivo:
        return json.load(leerArchivo)
    

def actualizarJson(nombreArchivo:str, informacion:dict):
    with open(RUTA_BASE+nombreArchivo, 'w+', encoding='utf-8') as actualizarArchivo:
        json.dump(informacion,actualizarArchivo,indent=4)