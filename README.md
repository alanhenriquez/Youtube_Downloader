# Descargador de Videos de YouTube

Este es un simple script en Python para descargar videos y listas de reproducción de YouTube utilizando la librería Pytube. El script permite al usuario elegir entre descargar un video individual o una lista de reproducción completa, con opciones para descargar en formato MP4, MP3 o ambos.

## Requisitos

- (REQUERIDO) Python 3.11.0 en adelante

- (REQUERIDO) Habilitar la ejecución de scripts en PowerShell:

    Para activar el entorno virtual en PowerShell, es necesario cambiar la política de ejecución de scripts. Sigue estos pasos:

    1. Abre PowerShell como administrador:
        - Haz clic derecho en el menú de inicio y selecciona "Windows PowerShell (Administrador)".

    2. Cambia la política de ejecución ejecutando el siguiente comando:
        ```sh
        Set-ExecutionPolicy RemoteSigned
        ```

    3. Confirma el cambio escribiendo `Y` y presionando Enter.

    Después de activar el entorno virtual, puedes restaurar la política de ejecución a su configuración original (No recomendado si lo piensas utilizar seguido, o tendras que repetir el proceso para permitir la ejecución de scripts en PowerShell):
    ```sh
    Set-ExecutionPolicy Restricted
    ```

- (REQUERIDO) Crear y activar un entorno virtual:

    1. Clona este repositorio.
    2. Abre una terminal CMD o PowerShell y navega hasta el directorio del proyecto.
    3. Ejecuta el script `setup_venv.py` para crear y configurar el entorno virtual:

        ```sh
        python setup_venv.py
        ```

- (NO TE PREOCUPES POR ESTA PARTE MIENTRAS QUE DESCARGUES TODOS LOS ARCHIVOS DEL REPOSITORIO)

- Pytube: La librería Pytube debe estar instalada en el entorno virtual. El script `setup_venv.py` se encargará de esto.

- Colorama: La librería Colorama también debe estar instalada en el entorno virtual. El script `setup_venv.py` se encargará de esto.

## Uso

1. Clona este repositorio.
2. Ejecuta el script `setup_venv.py` como se describe en los requisitos. (Si ya lo hiciste en los requerimientos, puedes saltarte este paso).
3. Abre una terminal CMD o PowerShell y navega hasta donde se encuentra el archivo `downloader.py` dentro del entorno virtual (`venv_downloader`).
4. Activa el entorno virtual:

    ```sh
    .\Scripts\activate
    ```

5. Ejecuta el script utilizando Python:

    ```sh
    python downloader.py
    ```

6. Selecciona una de las opciones:

    - **1: Descargar video**: Para descargar un video de YouTube.
    - **2: Descargar lista de reproducción**: Para descargar una lista de reproducción completa.
    - **q: Salir**: Para salir del programa.

7. Sigue las instrucciones en la terminal para ingresar la URL del video o de la lista de reproducción, el formato de descarga y la ruta de descarga.

## Ejemplos

- Descargar un video:

    ```sh
    ¿Qué deseas hacer? (1: Descargar video / 2: Descargar lista de reproducción / q: Salir): 1
    Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=VIDEO_ID
    Seleccione el formato de descarga (mp4 / mp3 / ambos): mp4
    Ingresa la ruta donde deseas guardar el video o audio (puede ser una carpeta): /ruta/a/la/carpeta
    ```

- Descargar una lista de reproducción:

    ```sh
    ¿Qué deseas hacer? (1: Descargar video / 2: Descargar lista de reproducción / q: Salir): 2
    Ingresa el enlace de la lista de reproducción de YouTube: https://www.youtube.com/playlist?list=PLAYLIST_ID
    Seleccione el formato de descarga (mp4 / mp3 / ambos): mp3
    Ingresa la ruta donde deseas guardar los videos o audios (puede ser una carpeta): /ruta/a/la/carpeta
    ```

## Notas

- Si un video o lista de reproducción está marcado como privado o no está disponible, el programa mostrará un mensaje de advertencia y no intentará descargarlo.
- Si experimentas algún problema, asegúrate de tener una conexión a internet estable y de que la URL que ingresaste sea válida.

¡Disfruta descargando tus videos favoritos de YouTube!
