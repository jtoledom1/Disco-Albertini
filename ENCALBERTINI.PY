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

# Función para pedir al usuario la configuración del disco y el mensaje
def pedir_configuracion():
    """
    Función que solicita al usuario el mensaje y el desplazamiento del disco.
    """
    mensaje = input("Introduce el mensaje a encriptar: ")
    while True:
        try:
            offset = int(input("Introduce el desplazamiento del disco (0-25): "))
            if 0 <= offset <= 25:
                break
            else:
                print("Por favor, introduce un número entre 0 y 25.")
        except ValueError:
            print("Por favor, introduce un número válido entre 0 y 25.")
    
    mensaje_encriptado = encriptar(mensaje, offset)
    print(f"Mensaje encriptado: {mensaje_encriptado}")

# Llamar a la función principal
if __name__ == "__main__":
    pedir_configuracion()
