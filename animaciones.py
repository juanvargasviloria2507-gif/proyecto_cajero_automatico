import time
import sys
from colores import *

def cargando(texto="Procesando"):
    """
    Muestra una animación de carga con puntos.
    """
    for i in range(3):
        sys.stdout.write(Fore.CYAN + f"\r{texto}{'.'*i}" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.5)
    print()  # Salto de línea al final

def bienvenida():
    """
    Muestra el mensaje de bienvenida del cajero con colores.
    """
    print(titulo("\n=============================="))
    print(titulo("   BIENVENIDO AL CAJERO ATM"))
    print(titulo("==============================\n") )

def despedida():
    """
    Muestra un mensaje de despedida colorido
    """
    print(magenta ("\n=============================="))
    print(magenta("GRACIAS POR USAR EL CAJERO"))
    print(magenta("==============================\n") )
