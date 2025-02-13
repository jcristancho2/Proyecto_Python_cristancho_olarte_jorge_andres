# Importa las funciones necesarias desde diferentes módulos
import module.utils.control_screen as cc
import module.utils.validate_data as vd
#from module.controllers.mainMenuController import menu
import module.ui.menu as mm
import module.create_json.file_json as jj

def search_element():
    """
    Muestra un menú para buscar elementos.
    """
    cc.deleteScreen()  # Limpia la pantalla
    
    print(mm.search_element)  # Muestra el menú
    
    # Pide al usuario que elija una opción y la valida
    option = int(vd.validateInt('Selecciona una opción ⏩  '))
    
    match option:
        case 1:
            jj.mostrarelementoTable()  # Muestra elemento en tabla
        case 2:
            jj.mostrarelementoautor()  # Muestra elemento por autor
        case 3:
            jj.mostrarelementogenero()  # Muestra elemento por género
        case 4:
            print('Regresando al Menú Anterior')  # Opción para salir del menú
            return
        case _:
            cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
            print('Opción inválida')
