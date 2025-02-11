
import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
from main import ERROR, menu, NAME
import module.create_json.file_json as fj

import os
import json
from typing import Dict, List, Optional 

data = []

def register ():
    cc.deleteScreen()
    print(mm.add_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            library()
        case 2 :
            music()
        case 3 :
            movie()
        case 4 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)
            
"""//////////////////////////////////////////////////////////////////"""
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

"""//////////////////////////////////////////////////////////////////"""

def view_elements ():
    cc.deleteScreen()
    print(mm.view_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)
            
def search_element ():
    cc.deleteScreen()
    print(mm.search_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)
            
def edit_element ():
    cc.deleteScreen()
    print(mm.edit_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            pass
        case 5 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)
            
def delete_element ():
    cc.deleteScreen()
    print(mm.delete_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)
            
def view_element_category ():
    cc.deleteScreen()
    print(mm.view_element_category)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)            

def save_load_element():
    cc.deleteScreen()
    print(mm.save_load_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            print('Regresando al Menú Anterior')
            return menu()
        case _:
            print(ERROR)   



# from modules.utils.controlScreen import deleteScreen as clean, pauseScreen as pause 
# from modules.creacionJson.archivosJson import crearJson, leerJson, actualizarJson, guardarDict
# def crearTeam()->None:
#     clean()
#     crearJson('coleccion.json')
#     coleccionJson=leerJson('coleccion.json')
#     Libros={
#         "libro":{
#         },
#     }
#     clean()
#     nlibro=str(input(f'Ingrese el nombre del libro: '))
#     coleccionJson.update({Libros:["libro"]:nlibro})
#     actualizarJson('coleccion.json', coleccionJson)