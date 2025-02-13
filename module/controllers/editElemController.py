import module.utils.control_screen as cc
import module.utils.validate_data as vd
import module.ui.menu as mm
import module.create_json.file_json as jj

def editElemento():
    while True:
        cc.deleteScreen()
        print(mm.edit_element)
        opcSel=int(vd.validateInt('Seleccione la opción que desea realizar: '))
        match opcSel:
            case 1:
                jj.editarNom()
            case 2:
                jj.editId()
            case 3:
                jj.editarGenero()
            case 4:
                jj.editarValoracion()
            case 5:
                return
            case _:
                cc.deleteScreen()
                print('invalid option')
                cc.pauseScreen()
                return