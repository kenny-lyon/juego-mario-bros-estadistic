import pygame
import os

def cargar_imagen(nombre, carpeta="D:/Mario Bros Proyecto/recursos/imagenes/jugador"):
    """
    Carga una imagen desde la carpeta especificada.

    :param nombre: Nombre del archivo de la imagen.
    :param carpeta: Carpeta donde se encuentra la imagen.
    :return: Superficie de Pygame con la imagen cargada.
    """
    ruta = os.path.join(carpeta, nombre)
    try:
        imagen = pygame.image.load(ruta).convert_alpha()  # Usa convert_alpha para manejar transparencias
        return imagen
    except pygame.error as e:
        print(f"No se pudo cargar la imagen: {ruta}")
        raise SystemExit(e)
