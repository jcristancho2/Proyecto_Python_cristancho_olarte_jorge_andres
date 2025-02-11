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
# import module.create_json.file_json as 
#from module.controllers.funtions import register
import module.controllers.funtions as ff
ERROR = 'option invalid'

def menu ():
    
    cc.deleteScreen()
    print(mm.admin_collection)
    option = int(vd.validateInt(f'Selecciona una opción ⏩  ' ))
    match option:
        case 1 :
            cc.deleteScreen()
            ff.register()
        case 2 :
            cc.deleteScreen()
            print(mm.view_element)
        case 3 :
            cc.deleteScreen()
            print(mm.search_elementhe)
        case 4 :
            cc.deleteScreen()
            print(mm.edit_element)
        case 5 :
            cc.deleteScreen()
            print(mm.delete_element)
        case 6 :
            cc.deleteScreen()
            print(mm.view_element_category)
        case 7 :
            cc.deleteScreen()
            print(mm.save_load_elementsave_)
        case 8 :
            cc.deleteScreen()
            exit
        case _:
            cc.deleteScreen()
            print(ERROR)
    

if __name__=='__main__':
    menu()

