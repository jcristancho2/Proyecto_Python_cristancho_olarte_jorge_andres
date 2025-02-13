# Importa las funciones necesarias desde diferentes módulos
import module.utils.control_screen as cc
import module.utils.validate_data as vd
#from module.controllers.mainMenuController import menu
import module.ui.menu as mm
import module.create_json.file_json as jj

def save_load_element():
    """
    Muestra un menú para guardar o cargar elementos.
    """
    cc.deleteScreen()  # Limpia la pantalla

    print(mm.save_load_element)  # Muestra el menú

    # Pide al usuario que elija una opción y la valida
    option = int(vd.validateInt('Selecciona una opción ⏩  '))
    
    match option:
        case 1:
            jj.savecolecction()  # Guarda la colección
        case 2:
            jj.loadcolecction()  # Carga la colección
        case 3:
            print('Regresando al Menú Anterior')  # Opción para salir del menú
            return
        case _:
            cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
            print('Opción inválida')
            cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
