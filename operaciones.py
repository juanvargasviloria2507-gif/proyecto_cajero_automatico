###1 
import json
from colores import correcto, error, advertencia
from animaciones import cargando


with open("datoscajero.json", "r") as archivo:
    datos = json.load(archivo)

def validar_pin(usuario):

    # verificar que el usuario exista y no sea "cajero"
    while usuario not in datos or usuario == "cajero":
        print(error("Usuario no válido, intente nuevamente: "))
        usuario=input("")
        

    intentos = 0

    while intentos < datos[usuario]["limite_intentos"]:

        pin_usuario = input("Ingrese su PIN: ")

        if pin_usuario == datos[usuario]["pin"]:
            print(correcto("PIN correcto"))
            return True

        intentos += 1
        restantes = datos[usuario]["limite_intentos"] - intentos
        print(error(f"PIN incorrecto. Intentos restantes: {restantes}"))

    print(error("Cuenta bloqueada por demasiados intentos"))
    return False

def consultar_saldo(usuario):
    cargando()
    print(correcto(f"Tu saldo es: ${datos[usuario]["saldo"]}"))
    datos[usuario]["movimientos"].append("Consulta de saldo")

def retirar_dinero(usuario):

    try:
        monto = int(input("Monto a retirar: "))
    except ValueError:
        print(error("Debe ingresar un número válido"))
        return

    if monto <= 0:
        print(error("Monto inválido"))
        return

    if monto > datos[usuario]["saldo"]:
        print(error("Saldo insuficiente"))
        return

    if monto > datos["cajero"]["efectivo_disponible"]:
        print(error("El cajero no tiene suficiente efectivo"))
        return

    datos[usuario]["saldo"] -= monto
    datos["cajero"]["efectivo_disponible"] -= monto
    datos[usuario]["retirado_hoy"] += monto
    datos[usuario]["movimientos"].append(f"Retiro: ${monto}")

    cargando()
    print(correcto("Retiro exitoso"))

    