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

    # guardar cambios
    with open("datoscajero.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def retiro_rapido(usuario):

    print("""
1. $200
2. $500
3. $700
4. $1000
""")

    opcion = input("Seleccione monto a retirar: ")

    montos = {
        "1": 200,
        "2": 500,
        "3": 700,
        "4": 1000
    }

    if opcion not in montos:
        print(error("Opción inválida"))
        return

    monto = montos[opcion]

    if monto > datos[usuario]["saldo"]:
        print(error("Saldo insuficiente"))
        return

    if datos[usuario]["retirado_hoy"] + monto > datos[usuario]["limite_diario"]:
        print(advertencia("Supera el límite diario"))
        return
    datos[usuario]["saldo"] -= monto
    datos[usuario]["retirado_hoy"] += monto
    datos["cajero"]["efectivo_disponible"] -= monto

    datos[usuario]["movimientos"].append(f"Retiro Rapido: ${monto}")

    cargando()
    print(correcto("Retiro rápido exitoso"))

    # guardar cambios
    with open("datoscajero.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    
 ##3

def depositar_dinero(usuario):
    monto = int(input("Monto a depositar: "))

    if monto <= 0:
        print(error("Monto inválido"))
        return

    datos[usuario]["saldo"]  += monto
    datos[usuario]["movimientos"].append(f"Deposito: ${monto}")
    # guardar cambios
    with open("datoscajero.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    cargando()
    print(correcto("Depósito exitoso"))

def consultar_movimientos(usuario):
    print("\n==== HISTORIAL ====")

    if not datos[usuario]["movimientos"]:
        print("No hay movimientos aún")
    else:
        for m in datos[usuario]["movimientos"]:
            print(m)

    print("===================\n")

    