from pytube import YouTube, Playlist
from colorama import Fore, Style, init
import re
import os

# Inicializar Colorama para Windows
init(convert=True)

def verificar_privacidad(url):
    try:
        if "/watch?" in url:
            video = YouTube(url)
            if video.player_response['playabilityStatus']['status'] == 'ERROR':
                print(Fore.RED + "El video está marcado como privado o no está disponible." + Style.RESET_ALL)
                return False
        elif "list=" in url:
            playlist = Playlist(url)
            if len(playlist.video_urls) == 0:
                print(Fore.RED + "La lista de reproducción está marcada como privada o no está disponible." + Style.RESET_ALL)
                return False
        return True
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)
        return False


def descargar_video(url, ruta_descarga, formato):
    try:
        # Instancia un objeto YouTube con la URL del video
        video = YouTube(url)

        # Eliminar caracteres especiales del título del video
        titulo_limpio = re.sub(r'[<>:"/\\|?*]', '', video.title)

        # Verificar si el archivo ya existe en la carpeta de destino
        archivo_existente = f"{titulo_limpio}.{formato}" in os.listdir(ruta_descarga)

        if archivo_existente:
            print(Fore.YELLOW + f"El archivo '{titulo_limpio}.{formato}' ya existe en la carpeta de destino. Saltando descarga." + Style.RESET_ALL)
            return

        if formato == "mp4":
            # Descarga el video en formato MP4
            stream = video.streams.get_highest_resolution()
            print(Fore.GREEN + f"Descargando '{titulo_limpio}' en formato MP4..." + Style.RESET_ALL)
            stream.download(ruta_descarga)
            print(Fore.GREEN + "Descarga completada." + Style.RESET_ALL)
        elif formato == "mp3":
            # Descarga solo el audio en formato MP3
            audio_stream = video.streams.filter(only_audio=True).first()
            print(Fore.GREEN + f"Descargando el audio de '{titulo_limpio}' en formato MP3..." + Style.RESET_ALL)
            audio_stream.download(output_path=ruta_descarga, filename=f"{titulo_limpio}.mp3")
            print(Fore.GREEN + "Descarga completada." + Style.RESET_ALL)
        elif formato == "ambos":
            # Descarga tanto el video en formato MP4 como el audio en formato MP3
            stream = video.streams.get_highest_resolution()
            print(Fore.GREEN + f"Descargando '{titulo_limpio}' en formato MP4..." + Style.RESET_ALL)
            stream.download(ruta_descarga, filename=f"{titulo_limpio}.mp4")
            print(Fore.GREEN + "Descarga de video completada." + Style.RESET_ALL)
            audio_stream = video.streams.filter(only_audio=True).first()
            print(Fore.GREEN + f"Descargando el audio de '{titulo_limpio}' en formato MP3..." + Style.RESET_ALL)
            audio_stream.download(output_path=ruta_descarga, filename=f"{titulo_limpio}.mp3")
            print(Fore.GREEN + "Descarga de audio completada." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)


def descargar_lista_reproduccion(url, ruta_descarga, formato):
    try:
        # Instancia un objeto Playlist con la URL de la lista de reproducción
        playlist = Playlist(url)

        # Lista para almacenar los títulos y formatos de los archivos existentes en la carpeta de destino
        archivos_existentes = [file.lower() for file in os.listdir(ruta_descarga)]

        # Descarga cada video de la lista de reproducción
        for i, video in enumerate(playlist.videos, start=1):
            # Eliminar caracteres especiales del título del video
            titulo_limpio = re.sub(r'[<>:"/\\|?*]', '', video.title)

            # Agregar el índice al inicio del título
            titulo_con_indice = f"{i:03d} - {titulo_limpio}"

            # Verificar si el archivo ya existe en la carpeta de destino
            archivo_existente = any(titulo_con_indice.lower() in archivo for archivo in archivos_existentes)

            if archivo_existente:
                print(Fore.YELLOW + f"El archivo '{titulo_con_indice}.{formato}' ya existe en la carpeta de destino. Saltando descarga." + Style.RESET_ALL)
                continue

            try:
                if formato == "mp4":
                    # Descarga el video en formato MP4
                    stream = video.streams.get_highest_resolution()
                    print(Fore.GREEN + f"Descargando '{titulo_con_indice}' en formato MP4..." + Style.RESET_ALL)
                    filename = f"{titulo_con_indice}.mp4"  # Añadir el índice al nombre del archivo
                    stream.download(ruta_descarga, filename=filename)
                    print(Fore.GREEN + "Descarga completada." + Style.RESET_ALL)
                elif formato == "mp3":
                    # Descarga solo el audio en formato MP3
                    audio_stream = video.streams.filter(only_audio=True).first()
                    print(Fore.GREEN + f"Descargando el audio de '{titulo_con_indice}' en formato MP3..." + Style.RESET_ALL)
                    filename = f"{titulo_con_indice}.mp3"  # Añadir el índice al nombre del archivo
                    audio_stream.download(output_path=ruta_descarga, filename=filename)
                    print(Fore.GREEN + "Descarga completada." + Style.RESET_ALL)
                elif formato == "ambos":
                    # Descarga tanto el video en formato MP4 como el audio en formato MP3
                    stream = video.streams.get_highest_resolution()
                    print(Fore.GREEN + f"Descargando '{titulo_con_indice}' en formato MP4..." + Style.RESET_ALL)
                    video_filename = f"{titulo_con_indice}.mp4"  # Añadir el índice al nombre del archivo de video
                    stream.download(ruta_descarga, filename=video_filename)
                    print(Fore.GREEN + "Descarga de video completada." + Style.RESET_ALL)
                    
                    audio_stream = video.streams.filter(only_audio=True).first()
                    print(Fore.GREEN + f"Descargando el audio de '{titulo_con_indice}' en formato MP3..." + Style.RESET_ALL)
                    audio_filename = f"{titulo_con_indice}.mp3"  # Añadir el índice al nombre del archivo de audio
                    audio_stream.download(output_path=ruta_descarga, filename=audio_filename)
                    print(Fore.GREEN + "Descarga de audio completada." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ocurrió un error al descargar '{titulo_con_indice}': {e}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al procesar la lista de reproducción: {e}" + Style.RESET_ALL)


def menu():
    while True:
        opcion = input(Fore.MAGENTA + "¿Qué deseas hacer? (1: Descargar video / 2: Descargar lista de reproducción / q: Salir): " + Style.RESET_ALL)

        if opcion == "1":
            # Descarga de un solo video
            url = input("Ingresa la URL del video de YouTube: ")
            if url.lower() == "q":
                salir()
            if verificar_privacidad(url):
                formato = input("Seleccione el formato de descarga (mp4 / mp3 / ambos): ").lower()
                while formato not in ["mp4", "mp3", "ambos", "q"]:
                    print("Formato no válido. Por favor, seleccione 'mp4', 'mp3', 'ambos' o 'q' para salir.")
                    formato = input("Seleccione el formato de descarga (mp4 / mp3 / ambos): ").lower()
                if formato == "q":
                    salir()
                ruta_descarga = input("Ingresa la ruta donde deseas guardar el video o audio (puede ser una carpeta): ")
                if ruta_descarga.lower() == "q":
                    salir()
                descargar_video(url, ruta_descarga, formato)
        elif opcion == "2":
            # Descarga de una lista de reproducción
            url_lista = input("Ingresa el enlace de la lista de reproducción de YouTube: ")
            if url_lista.lower() == "q":
                salir()
            if verificar_privacidad(url_lista):
                formato = input("Seleccione el formato de descarga (mp4 / mp3 / ambos): ").lower()
                while formato not in ["mp4", "mp3", "ambos", "q"]:
                    print("Formato no válido. Por favor, seleccione 'mp4', 'mp3', 'ambos' o 'q' para salir.")
                    formato = input("Seleccione el formato de descarga (mp4 / mp3 / ambos): ").lower()
                if formato == "q":
                    salir()
                ruta_descarga = input("Ingresa la ruta donde deseas guardar los videos o audios (puede ser una carpeta): ")
                if ruta_descarga.lower() == "q":
                    salir()
                descargar_lista_reproduccion(url_lista, ruta_descarga, formato)
        elif opcion.lower() == "q":
            salir()
        else:
            print("Opción no válida. Por favor, selecciona '1', '2' o 'q'.")


def salir():
    print(Fore.YELLOW + "Saliendo del programa..." + Style.RESET_ALL)
    exit()


if __name__ == "__main__":
    print(Fore.CYAN + "Bienvenido al descargador de videos de YouTube!" + Style.RESET_ALL)
    menu()
