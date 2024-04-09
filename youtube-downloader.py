from pytube import YouTube
import os

def youtube_download(archivo_txt):
    # Comprobamos si el archivo existe
    if not os.path.exists(archivo_txt):
        print(f"El archivo '{archivo_txt}' no existe.")
        return
    
    # Carpeta download
    carpeta_download = "download"
    if not os.path.exists(carpeta_download):
        os.makedirs(carpeta_download)
        print(f"Se ha creado carpeta de descargas: {carpeta_download}")
        
    # Abrir el archivo de texto y leer los enlaces
    with open(archivo_txt, 'r') as file:
        enlaces = file.readlines()
    
    # Iterar sobre los enlaces
    for enlace in enlaces:
        try:
            yt = YouTube(enlace)
            # Descargar el video en la máxima calidad disponible
            video = yt.streams.get_highest_resolution()
            video.download(output_path=carpeta_download)
            print(f"Video '{yt.title}' descargado en {carpeta_download}")
        except Exception as e:
            print(f"Error al descargar el video desde {enlace}: {e}")

# Archivo de texto que contiene los enlaces de los videos
archivo_txt = "videos.txt"
# Llamada a la función para descargar los videos
youtube_download(archivo_txt)