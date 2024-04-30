# Descargador de Videos de YouTube

Este es un simple script en Python para descargar videos y listas de reproducción de YouTube utilizando la librería Pytube. El script permite al usuario elegir entre descargar un video individual o una lista de reproducción completa, con opciones para descargar en formato MP4, MP3 o ambos.

## Requisitos

- (REQUERIDO) Python 3.11.0 en adelante

- (NO TE PREOCUPES POR ESTA PARTE MIENTRAS QUE DESCARGUES TODOS LOS ARCHIVOS DEL REPOSITORIO)

- Pytube: La librería Pytube debe estar instalada. Puede instalarla utilizando pip:

    ```
    pip install pytube
    ```

- Colorama: La librería Colorama también debe estar instalada para mostrar mensajes en colores. Puede instalarla utilizando pip:

    ```
    pip install colorama
    ```

## Uso

1. Clona este repositorio.
2. Abre una terminal CMD y navega hasta donde se encuentra el archivo `downloader.py`.
3. Escribe en tu terminal CMD lo siguiente:

    ```
    .\Scripts\activate
    ```

4. Ejecuta el script utilizando Python:

    ```
    python downloader.py
    ```

5. Selecciona una de las opciones:

    - **1: Descargar video**: Para descargar un video de YouTube.
    - **2: Descargar lista de reproducción**: Para descargar una lista de reproducción completa.
    - **q: Salir**: Para salir del programa.

6. Sigue las instrucciones en la terminal para ingresar la URL del video o de la lista de reproducción, el formato de descarga y la ruta de descarga.

## Ejemplos

- Descargar un video:

    ```
    ¿Qué deseas hacer? (1: Descargar video / 2: Descargar lista de reproducción / q: Salir): 1
    Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=VIDEO_ID
    Seleccione el formato de descarga (mp4 / mp3 / ambos): mp4
    Ingresa la ruta donde deseas guardar el video o audio (puede ser una carpeta): /ruta/a/la/carpeta
    ```

- Descargar una lista de reproducción:

    ```
    ¿Qué deseas hacer? (1: Descargar video / 2: Descargar lista de reproducción / q: Salir): 2
    Ingresa el enlace de la lista de reproducción de YouTube: https://www.youtube.com/playlist?list=PLAYLIST_ID
    Seleccione el formato de descarga (mp4 / mp3 / ambos): mp3
    Ingresa la ruta donde deseas guardar los videos o audios (puede ser una carpeta): /ruta/a/la/carpeta
    ```

## Notas

- Si un video o lista de reproducción está marcado como privado o no está disponible, el programa mostrará un mensaje de advertencia y no intentará descargarlo.
- Si experimentas algún problema, asegúrate de tener una conexión a internet estable y de que la URL que ingresaste sea válida.

¡Disfruta descargando tus videos favoritos de YouTube!
