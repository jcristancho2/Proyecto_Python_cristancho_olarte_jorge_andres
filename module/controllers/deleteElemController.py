# Importa las funciones necesarias desde diferentes módulos
import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
import module.create_json.file_json as jj

def deleteElemento():
    """
    Muestra un menú para que el usuario elimine diferentes tipos de elementos.
    """
    while True:
        cc.deleteScreen()  # Limpia la pantalla
        
        print(mm.delete_element)  # Muestra el menú
        
        # Pide al usuario que elija una opción y la valida
        opcSel = int(vd.validateInt('Seleccione la opción que desea realizar: '))
        
        match opcSel:
            case 1:
                jj.eliminarElemXnom()  # Elimina un elemento por nombre
            case 2:
                jj.eliminarXid()  # Elimina un elemento por ID
            case 3:
                print('Regresando al Menú Anterior')  # Opción para salir del menú
                return
            case _:
                cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
                print('Opción inválida')
                cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
