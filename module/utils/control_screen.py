from os import system
import sys

def deleteScreen():
    """
    Limpia la pantalla dependiendo del sistema operativo.
    """
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pauseScreen():
    """
    Pausa la ejecución del programa esperando una acción del usuario, dependiendo del sistema operativo.
    """
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presione una tecla para continuar")
    else:
        system("pause")
