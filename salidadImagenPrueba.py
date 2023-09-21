#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
import os

import requests
from PIL import Image
from io import BytesIO

directorio_actual = os.path.dirname(os.path.abspath(__file__))
nombre_imagen = "ImagenPrueba.jpg"

url = "https://xsgames.co/randomusers/avatar.php?g=male"

class MiApp:
    def __init__(self):
        # Crear la ventana
        self.ventana = Gtk.Window(title="Mostrar Imagen")
        self.ventana.connect("destroy", Gtk.main_quit)
        self.ventana.set_default_size(400, 400)

        # Crear una rejilla
        self.rejilla = Gtk.Grid()
        self.ventana.add(self.rejilla)

        # Crear un botón y agregarlo a la rejilla
        self.boton_mostrar_imagen = Gtk.Button(label="Mostrar Imagen")
        self.boton_mostrar_imagen.connect("clicked", self.mostrar_imagen)
        self.rejilla.attach(self.boton_mostrar_imagen, 0, 0, 1, 1)

        # Crear un contenedor para la imagen
        self.contenedor_imagen = Gtk.Box()
        self.rejilla.attach(self.contenedor_imagen, 0, 1, 1, 1)

        # Crear un objeto de imagen
        self.imagen = Gtk.Image()
        self.contenedor_imagen.pack_start(self.imagen, True, True, 0)

    def mostrar_imagen(self, widget):
        # Cargar y mostrar la imagen
        #ruta_imagen = os.path.join(directorio_actual, nombre_imagen)  # Reemplaza con la ruta de tu imagen
        #pixbuf = GdkPixbuf.Pixbuf.new_from_file(ruta_imagen)

        response = requests.get(url)
        imagen_bytes = BytesIO(response.content)

        # Abrir la imagen con PIL
        imagen_pil = Image.open(imagen_bytes)

        # Convertir la imagen a un GdkPixbuf
        imagen_gdk = GdkPixbuf.Pixbuf.new_from_data(
            imagen_pil.tobytes(), GdkPixbuf.Colorspace.RGB, False,
            imagen_pil.bits, imagen_pil.width, imagen_pil.height,
            imagen_pil.width * 3
        )

        self.imagen.set_from_pixbuf(imagen_gdk)

    def run(self):
        self.ventana.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = MiApp()
    app.run()