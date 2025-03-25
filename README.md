

# Disco de Alberti - Cifrado y Descifrado

Este repositorio implementa el **Cifrado de Alberti** utilizando dos discos rotatorios para encriptar y desencriptar mensajes. El programa está escrito en Python y permite al usuario seleccionar el desplazamiento para configurar el disco y cifrar o descifrar mensajes de texto.

## Funciones principales

- **Encriptar mensaje**: Usando el Cifrado de Alberti, el programa convierte un mensaje en texto claro en su versión cifrada.
- **Desencriptar mensaje**: Usando el mismo mecanismo de cifrado, el programa puede restaurar un mensaje cifrado a su forma original.
- **Menú interactivo**: El usuario puede elegir entre encriptar, desencriptar o salir, con opciones fáciles de usar en un menú.

## Requisitos

- **Python 3.x**: Este código ha sido probado con Python 3.x.
- **Biblioteca estándar**: No se requieren bibliotecas externas, ya que el programa utiliza solo la biblioteca estándar de Python.

## Instrucciones para usar

1. **Clona el repositorio**:

   Si aún no tienes el repositorio clonado, puedes hacerlo usando `git`:

   ```bash
   git clone https://github.com/jtoledom1/Disco-Albertini.git
   ```

2. **Ejecuta el script**:

   Navega hasta la carpeta del repositorio y ejecuta el archivo Python con el siguiente comando:

   ```bash
   python3 disco_alberti.py
   ```

3. **Selecciona una opción**:

   El programa te mostrará un menú con tres opciones:

   ```
   --- Menú ---
   1. Encriptar mensaje
   2. Desencriptar mensaje
   3. Salir
   ```

   - **Opción 1**: Encriptar mensaje: Te pedirá que ingreses un mensaje y un desplazamiento para el disco. El desplazamiento debe estar entre 0 y 25.
   - **Opción 2**: Desencriptar mensaje: Te pedirá que ingreses un mensaje cifrado y el desplazamiento correspondiente para descifrarlo.
   - **Opción 3**: Salir: Cierra el programa.

4. **Resultado**:

   Después de encriptar o desencriptar el mensaje, el programa te mostrará el resultado.

   Ejemplo de salida:
   ```
   --- Menú ---
   1. Encriptar mensaje
   2. Desencriptar mensaje
   3. Salir
   Selecciona una opción (1/2/3): 1
   Introduce el mensaje: HELLO
   Introduce el desplazamiento del disco (0-25): 3
   Mensaje encriptado: KHOOR
   ```

   Y si eliges desencriptar:
   ```
   --- Menú ---
   1. Encriptar mensaje
   2. Desencriptar mensaje
   3. Salir
   Selecciona una opción (1/2/3): 2
   Introduce el mensaje: KHOOR
   Introduce el desplazamiento del disco (0-25): 3
   Mensaje desencriptado: HELLO
   ```

## ¿Cómo funciona el Cifrado de Alberti?

El **Cifrado de Alberti** es un cifrado de sustitución polialfabético. Utiliza dos discos rotatorios, uno fijo y otro rotatorio, que contienen el alfabeto. El disco rotatorio se ajusta según un desplazamiento dado por el usuario, y cada letra del mensaje se sustituye por la letra correspondiente en el disco rotatorio.

### Descripción de los discos:

- **Disco fijo**: Contiene el alfabeto estándar (A-Z).
- **Disco rotatorio**: Es igual al disco fijo, pero rotado según el desplazamiento especificado.

Por ejemplo, si el desplazamiento es 3, el alfabeto en el disco rotatorio sería:
```
DEFGHIJKLMNOPQRSTUVWXYZABC
```

Cada letra del mensaje original se sustituye por la letra en la misma posición en el disco rotatorio. Para desencriptar, se realiza el proceso inverso.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b nueva-caracteristica`).
3. Haz tus cambios y realiza commits (`git commit -am 'Añadir nueva característica'`).
4. Envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

¡Gracias por usar este proyecto y feliz encriptación!

