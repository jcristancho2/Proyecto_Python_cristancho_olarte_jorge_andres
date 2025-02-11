
import os
import json
from typing import Dict, List, Optional
import module.utils.control_screen as cc
import module.utils.validate_data as vd

from utils.control_screen import deleteScreen as clean, pauseScreen as pause 
from module.create_json.archivosJson import crearJson, leerJson, actualizarJson, guardarDict

data = {"libros": [], "musica": [], "peliculas": []}

def crearLibrary()->None:
    clean()
    crearJson('coleccion.json')
    coleccionJson=leerJson('coleccion.json')
    Libros={
        "libro":{
        },
    }
    clean()
    nlibro=str(input('Ingrese el nombre del libro: '))
    coleccionJson.update({Libros["libro"]:nlibro})
    actualizarJson('coleccion.json', coleccionJson)

def library ():
    cc.deleteScreen()
    libro = vd.validateAlnum(f'Escriba el nombre del libro ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {libro} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {libro} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {libro} '))
    
    data["libros"].append({
        "titulo": libro,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    })

def music ():
    cc.deleteScreen()
    cancion = vd.validateAlnum(f'Escriba el nombre del cancion ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {cancion} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {cancion} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {cancion} '))
    
    data["musica"].append({
        "titulo": cancion,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    })
    
def movie ():
    cc.deleteScreen()
    pelicula = vd.validateAlnum(f'Escriba el nombre del pelicula ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {pelicula} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {pelicula} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {pelicula} '))
    
    data["peliculas"].append({
        "titulo": pelicula,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    })