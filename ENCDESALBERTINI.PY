import string

# Función para crear el disco de Alberti
def crear_disco(offset):
    """
    Crear el disco de Alberti con un desplazamiento dado.
    """
    alfabeto = string.ascii_uppercase  # Usamos el alfabeto en mayúsculas
    disco_fijo = alfabeto
    disco_rotatorio = alfabeto[offset:] + alfabeto[:offset]
    return disco_fijo, disco_rotatorio

# Función para encriptar el mensaje
def encriptar(mensaje, offset):
    """
    Encriptar un mensaje usando el disco de Alberti.
    El parámetro 'offset' define el desplazamiento del disco rotatorio.
    """
    disco_fijo, disco_rotatorio = crear_disco(offset)
    mensaje = mensaje.upper().replace(" ", "")  # Convertimos el mensaje a mayúsculas y eliminamos espacios
    mensaje_encriptado = []

    for letra in mensaje:
        if letra in disco_fijo:
            # Encontrar la posición de la letra en el disco fijo
            index = disco_fijo.index(letra)
            # Encriptar la letra con el disco rotatorio
            mensaje_encriptado.append(disco_rotatorio[index])
    
    return ''.join(mensaje_encriptado)

# Función para desencriptar el mensaje
def desencriptar(mensaje, offset):
    """
    Desencriptar un mensaje usando el disco de Alberti.
    El parámetro 'offset' define el desplazamiento del disco rotatorio.
    """
    disco_fijo, disco_rotatorio = crear_disco(offset)
    mensaje = mensaje.upper().replace(" ", "")  # Convertimos el mensaje a mayúsculas y eliminamos espacios
    mensaje_desencriptado = []

    for letra in mensaje:
        if letra in disco_rotatorio:
            # Encontrar la posición de la letra en el disco rotatorio
            index = disco_rotatorio.index(letra)
            # Desencriptar la letra con el disco fijo
            mensaje_desencriptado.append(disco_fijo[index])
    
    return ''.join(mensaje_desencriptado)

# Función para pedir al usuario la configuración del disco y el mensaje a encriptar o desencriptar
def pedir_configuracion(opcion):
    """
    Función que solicita al usuario el mensaje y el desplazamiento del disco para encriptar o desencriptar.
    """
    mensaje = input("Introduce el mensaje: ")
    while True:
        try:
            offset = int(input("Introduce el desplazamiento del disco (0-25): "))
            if 0 <= offset <= 25:
                break
            else:
                print("Por favor, introduce un número entre 0 y 25.")
        except ValueError:
            print("Por favor, introduce un número válido entre 0 y 25.")

    if opcion == 'encriptar':
        mensaje_encriptado = encriptar(mensaje, offset)
        print(f"Mensaje encriptado: {mensaje_encriptado}")
    elif opcion == 'desencriptar':
        mensaje_desencriptado = desencriptar(mensaje, offset)
        print(f"Mensaje desencriptado: {mensaje_desencriptado}")

# Menú para elegir la opción
def menu():
    """
    Menú para seleccionar la opción de encriptar, desencriptar o salir.
    """
    while True:
        print("\n--- Menú ---")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == '1':
            pedir_configuracion('encriptar')
        elif opcion == '2':
            pedir_configuracion('desencriptar')
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Llamar a la función principal del menú
if __name__ == "__main__":
    menu()
