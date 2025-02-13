# Importa las funciones necesarias desde diferentes módulos
import module.utils.control_screen as cc
import module.utils.validate_data as vd
#from module.controllers.mainMenuController import menu
import module.ui.menu as mm
import module.create_json.file_json as jj

def view_elements():
    """
    Muestra un menú para ver diferentes elementos.
    """
    cc.deleteScreen()  # Limpia la pantalla
    
    print(mm.view_element)  # Muestra el menú
    
    # Pide al usuario que elija una opción y la valida
    option = int(vd.validateInt('Selecciona una opción ⏩  '))
    
    match option:
        case 1:
            jj.mostrarLibraryTable()  # Muestra la tabla de la biblioteca
        case 2:
            jj.mostrarpeliTable()  # Muestra la tabla de películas
        case 3:
            jj.mostrarmusicTable()  # Muestra la tabla de música
        case 4:
            print('Regresando al Menú Anterior')  # Opción para salir del menú
            return
        case _:
            cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
            print('Opción inválida')
            cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
