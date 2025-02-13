"""

Fecha : 13/febrero/2025
nombre : collection_organizer
descripcion: 
"""
# Importa el módulo mainMenuController desde module.controllers y lo asigna a la variable main
import module.controllers.mainMenuController as main

# Comprueba si el archivo está siendo ejecutado directamente (no importado como un módulo)
if __name__ == '__main__':
    # Llama a la función menu() del módulo main
    main.menu()
    