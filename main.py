"""
Autor : jorge andres cristancho olarte
Fecha : 13/febrero/2025
nombre : collection_organizer
descripcion: 
"""
import os
import utils.control_screen as cc , utils.validate_data as vd
import module.ui.menu as mm
DESTINO = os.path.join('data/','organizer.json')
ERROR = 'option invalid'

def menu ():
    cc.deleteScreen()
    print(mm.admin_collection)
    option = int(vd.validateInt(f'Selecciona una opción ⏩' ))
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
            pass
        case 6 :
            pass
        case 7 :
            pass
        case 8 :
            pass
        case _:
            print(ERROR)
    

if __name__=='__main__':
    menu()