# Importa las funciones necesarias desde diferentes módulos
import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
import module.create_json.file_json as jj

def register():
    """
    Muestra un menú para que el usuario registre diferentes tipos de elementos.
    """
    while True:
        cc.deleteScreen()  # Limpia la pantalla
        
        print(mm.add_element)  # Muestra el menú
        
        # Pide al usuario que elija una opción y la valida
        option = int(vd.validateInt('Selecciona una opción ⏩  '))
        
        match option:
            case 1:
                jj.crearLibrary()  # Crea una biblioteca
            case 2:
                jj.crearPeli()  # Crea una película
            case 3:
                jj.crearMusic()  # Crea música
            case 4:
                print('Regresando al Menú Anterior...')  # Opción para salir del menú
                return
            case _:
                cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
                print('Opción inválida')
                cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
