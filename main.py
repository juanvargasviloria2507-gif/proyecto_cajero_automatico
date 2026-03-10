from animaciones import *
from operaciones import *
from colores import *


def menu():

    print(titulo("""
1. Cosultar saldo
2. Retirar dinero 
3. Retiro rapido
4. Depositar dinero
5. Consultar movimientos
6. salir
"""))
    
def main():
    bienvenida()
    while True:
        usuario = input("Ingrese su usuario: ")
        pin_correcto=validar_pin(usuario)
        while pin_correcto:

            menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                consultar_saldo(usuario)

            elif opcion == "2":
                retirar_dinero(usuario)

            elif opcion == "3":
                retiro_rapido(usuario)

            elif opcion == "4":
                depositar_dinero(usuario)

            elif opcion == "5":
                consultar_movimientos(usuario)

            elif opcion == "6":
                despedida()
                break

            else:
                print("Opcion invalida")

if __name__ == "__main__":
    main()