import time
from colorama import Fore, Style, init

init(autoreset=True)

def error(texto):
    return Fore.RED + texto + Style.RESET_ALL

def correcto(texto):
    return Fore.GREEN + texto + Style.RESET_ALL

def advertencia(texto):
    return Fore.YELLOW + texto + Style.RESET_ALL

def titulo(texto):
    return Fore.BLUE + texto + Style.RESET_ALL

def cyan(texto):
    return Fore.CYAN + texto + Style.RESET_ALL

def magenta(texto):
    return Fore.MAGENTA + texto + Style.RESET_ALL