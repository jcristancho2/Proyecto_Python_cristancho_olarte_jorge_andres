"""
Autor : jorge andres cristancho olarte
Fecha : 13/febrero/2025
nombre : collection_organizer
descripcion: 
"""
import os
import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
import module.controllers.funtions as f
import module.create_json.file_json as fj

NAME = os.path.join('data/','organizador.json')
ERROR = 'option invalid'

def menu ():
    cc.deleteScreen()
    print(mm.admin_collection)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            f.register()
        case 2 :
            f.view_elements()            
        case 3 :
            f.search_element()
        case 4 :
            f.edit_element()
        case 5 :
            f.delete_element()
        case 6 :
            f.view_element_category()
        case 7 :
            f.save_load_element()
        case 8 :
            cc.deleteScreen()
            exit
        case _:
            cc.deleteScreen()
            print(ERROR)
    

if __name__=='__main__':
    menu()

