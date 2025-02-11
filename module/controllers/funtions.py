
import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
from module.create_json.file_json import crearLibrary
from main import ERROR



def register ():
    print(mm.add_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            crearLibrary()
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            print('Regresando al Menú Anterior')
            return
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