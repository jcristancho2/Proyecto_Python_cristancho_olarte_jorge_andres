import utils.control_screen as cc , utils.validate_data as vd
import module.ui.menu as mm

ERROR = 'option invalid'

def register ():
    print(mm.add_element)
    option = int(vd.validateInt(f'Selecciona una opción ⏩' ))
    match option:
        case 1 :
            pass
        case 2 :
            pass
        case 3 :
            pass
        case 4 :
            print('Regresando al Menú Anterior')
            return
        case _:
            print(ERROR)

def library ():
    cc.deleteScreen()
    libro = vd.validateAlnum(f'Escriba el nombre del libro ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {libro} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {libro} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {libro} '))

def music ():
    cc.deleteScreen()
    cancion = vd.validateAlnum(f'Escriba el nombre del cancion ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {cancion} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {cancion} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {cancion} '))
    
def movie ():
    cc.deleteScreen()
    pelicula = vd.validateAlnum(f'Escriba el nombre del pelicula ')
    autor = vd.validateAlpha(f'Escriba el nombre del autor de {pelicula} ')
    genero =vd.validateAlpha(f'Escriba el nombre del genero de {pelicula} ')
    valoracion = int(vd.validateInt(f'Escriba el nombre del autor {pelicula} '))   