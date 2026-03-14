# Cajero Automático - Simulador ATM

Simulador de cajero automático desarrollado en Python con presentacion de consola colorida e interactiva.

## Descripción

Este proyecto simula las operaciones básicas de un cajero automático (ATM), contando con opciones y permitiendo a los usuarios realizar consultas de saldo, retiros, depósitos y consultar su historial de movimientos. El sistema cuenta validación de PIN, límites de retiro diario y control de efectivo disponible en el cajero.

## Características

- **Autenticación segura**: Validación de usuario y PIN con límite de intentos
- **Consulta de saldo**: Verifica tu saldo actual
- **Retiro de dinero**: Retira cantidad de dinero personalizada
- **Retiro rápido**: Opciones predefinidas ($200, $500, $700, $1000)
- **Depósito de dinero**: Incrementa tu saldo
- **Historial de movimientos**: Consulta todas tus transacciones
- **Interfaz colorida**: Mensajes con colores para mejor experiencia de usuario
- **Animaciones**: Efectos de carga para simular procesamiento

## Tecnologías

- **Python 3.x**
- **colorama**: Para colores en la consola
- **JSON**: Para almacenamiento de datos

## Instalación y uso del programa

1. Clona este repositorio:
```bash
1.1 Antes de clonar el repositorio; abrir la terminal; acontiuacion se dejaran una serie de comandos necesarios y paso a paso para poder ejecutar el programa correctamente (dependiendo del sistema operativo se deben usar distintos comandos en la terminal):

Windows
- Símbolo del sistema (CMD): Presiona Windows + R, escribe cmd y presiona Enter.

- Para acceder o posicionarte en una carpeta especifica ejecutar comando "cd (nombre de carpeta)"

MacOS
- Spotlight: Presiona "Comando + Espacio", "escribe Terminal" y "presiona Enter".

- Para acceder o posicionarte en una carpeta especifica ejecutar comando "cd (nombre de carpeta)"

Linux
- Atajo de teclado: Presiona "Ctrl + Alt + T" (funciona en la mayoría de distribuciones como Ubuntu).

- Menú de aplicaciones: Busca "Terminal" en el lanzador de aplicaciones.

- Para listar archivos en la terminal ejecutar el comando "ls" despues de haber ejecutado el comando, se debe visualizar todos los archivos y carpetas que estan en directorio actual.

- Para acceder o posicionarte en una carpeta especifica ejecutar comando "cd (nombre de carpeta)"

1.2 Ingresar este comando para poder clonar el repositorio git clone https://github.com/juanvargasviloria2507-gif/proyecto_cajero_automatico.git

Antes de poder clonar el repositorio y despues de haber accedido a la terminal ejecutar estos comandos (dependiendo nuestro sistema operativo) para poder listar o visualizar las carpetas o archivos que tienes en tu directorio actual (esto es importante porque queremos visualizar en que directorio o carpeta queremos clonar el repositorio; por ejemplo: Documentos, Escritorio, Descargas etc.).

Windows
- Para listar archivos en la terminal ejecutar el comando "dir" despues de haber ejecutado el comando, se debe visualizar todos los archivos y carpetas que estan en directorio actual. Despues de haber ejecutado ese comando ejecutamos este para que nos dirija o nos posicione a donde queremos colonar el repositorio "cd nombre del directorio o carpeta" por ejemplo: cd Documentos.

MacOS
- Para listar archivos en la terminal ejecutar el comando "ls" despues de haber ejecutado el comando, se debe visualizar todos los archivos y carpetas que estan en directorio actual. Despues de haber ejecutado ese comando ejecutamos este para que nos dirija o nos posicione a donde queremos colonar el repositorio "cd nombre del directorio o carpeta" por ejemplo: cd Documentos.

Linux
- Para listar archivos en la terminal ejecutar el comando "ls" despues de haber ejecutado el comando, se debe visualizar todos los archivos y carpetas que estan en directorio actual. Despues de haber ejecutado ese comando ejecutamos este para que nos dirija o nos posicione a donde queremos colonar el repositorio "cd nombre del directorio o carpeta" por ejemplo: cd Documentos.

1.3 Despues de haber clonado el repositorio cd proyecto_cajero_automatico al directorio escogido para poder ejecutar debemos entrar a la carpeta desde nuestra terminal y ejecutar los siguientes comandos python3 main.py (main.py es el programa inicial)
```

2. Instala las dependencias:
```bash
pip install colorama
```

## Uso del programa 

Ejecuta el programa principal:
```bash
python main.py
```

### Usuarios de prueba

El sistema incluye usuarios de prueba configurados en `datoscajero.json`:

| Usuario | PIN  | Saldo Inicial |
|---------|------|---------------|
| Juan    | 1234 | $500          |
| Migue   | 1235 | $1000         |

### Menú de opciones

1. **Consultar saldo**: Muestra el saldo actual de la cuenta
2. **Retirar dinero**: Permite retirar un monto personalizado
3. **Retiro rápido**: Opciones de retiro predefinidas
4. **Depositar dinero**: Añade dinero a tu cuenta
5. **Consultar movimientos**: Muestra el historial de transacciones
6. **Salir**: Cierra la sesión

## Estructura del Proyecto

```
proyecto_cajero_automatico/
│
├── main.py              # Archivo principal con el menú y flujo del programa
├── operaciones.py       # Lógica de las operaciones del cajero
├── animaciones.py       # Funciones de animación y mensajes
├── colores.py          # Funciones para colorear texto en consola
├── datoscajero.json    # Base de datos de usuarios y cajero
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo
```

## Seguridad

- **Límite de intentos**: Máximo 4 intentos para ingresar el PIN
- **Límite diario**: Control de retiro máximo por día ($1000)
- **Validación de saldo**: No permite retiros mayores al saldo disponible
- **Control de efectivo**: Verifica que el cajero tenga efectivo suficiente

## Persistencia de Datos

Los datos se almacenan en `datoscajero.json` y se guardan automáticamente después de cada transacción. El archivo cuenta con:

- Información de usuarios (saldo, PIN, movimientos)
- Límites de retiro diario
- Efectivo disponible en el cajero
- Historial de transacciones

## Características Visuales

El proyecto utiliza **colorama** para proporcionar una experiencia visual mejorada:

- 🔴 **Rojo**: Mensajes de error
- 🟢 **Verde**: Operaciones exitosas
- 🟡 **Amarillo**: Advertencias
- 🔵 **Azul**: Títulos y encabezados
- 🔷 **Cyan**: Prompts de entrada
- 🟣 **Magenta**: Mensajes de despedida

## Autor

Desarrollado como proyecto educativo para aprender Python y manejo de archivos JSON.

---

