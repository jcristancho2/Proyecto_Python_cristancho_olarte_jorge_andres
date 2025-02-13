# Importa las funciones necesarias desde diferentes módulos
import os
from module.utils import control_screen as cc
from module.utils import validate_data as vd
from module.ui import menu as mm
from module.controllers.addElemController import register
from module.controllers.deleteElemController import deleteElemento
from module.controllers.editElemController import editElemento
from module.controllers.saveloadElemController import save_load_element
from module.controllers.searchElemController import search_element
from module.controllers.viewElemController import view_elements
from module.controllers.viewCatElemController import view_element_category

def menu():
    """
    Muestra el menú principal para administrar la colección.
    """
    while True:
        cc.deleteScreen()  # Limpia la pantalla
        
        print(mm.admin_collection)  # Muestra el menú de administración
        
        # Pide al usuario que elija una opción y la valida
        option = int(vd.validateInt('Selecciona una opción ⏩  '))
        
        match option:
            case 1:
                register()  # Llama a la función para registrar elementos
            case 2:
                view_elements()  # Llama a la función para ver elementos
            case 3:
                search_element()  # Llama a la función para buscar elementos
            case 4:
                editElemento()  # Llama a la función para editar elementos
            case 5:
                deleteElemento()  # Llama a la función para eliminar elementos
            case 6:
                view_element_category()  # Llama a la función para ver categorías de elementos
            case 7:
                save_load_element()  # Llama a la función para guardar y cargar elementos
            case 8:
                cc.deleteScreen()  # Limpia la pantalla
                print('Saliendo...')
                cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
                break
            case _:
                cc.deleteScreen()  # Limpia la pantalla si la opción es inválida
                print('Opción inválida')
                cc.pauseScreen()  # Pausa la pantalla para que el usuario vea el mensaje
