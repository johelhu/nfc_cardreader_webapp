#!/usr/bin/env python 

import gi # librería de GimpToolKit
gi.require_version('Gtk', '3.0') # version necesaria para el programa
from gi.repository import Gtk # comandos GimpToolKit
from gi.repository import GLib as gl # se usa para editar la interfaz
import threading  # importa la biblioteca threading para trabajar con subprocesos
import signal # importa la biblioteca signal, modulo que permite trabajar con señales del sistema como Ctrl+C para interrumpir
import os # libreria para correr comandos bash dentro del codigo
from time import sleep # se usa para dar pausas sleep()

from lectorUID import leer # importa la funcion leer()

ventana = Gtk.Window(title="Lector de Tarjetas NFC") # iniciar una ventana
ventana.connect("destroy", Gtk.main_quit) # finalizar aplicación cuando se cierre la ventana
ventana.set_default_size(800, 600) # ajustar el tamaño de la ventana
# ventana.maximize() # maximizarlo a tamaño completo

rejilla = Gtk.Grid() # crea una rejilla con la clase Gtk.Grid
rejilla.get_style_context().add_class("rejilla_item") # la agrega a una clase css para darle estilos
ventana.add(rejilla) # mostrara la rejilla cuando se ejecute la aplicacion 

label1 = Gtk.Label(label="Lea la tarjeta NFC en el lector") # crear un label "etiqueta"
rejilla.attach(label1, 0, 0, 1, 1)  # Colocar label1 en la primera columna (0) y fila (0)

# se crean las etiquetas de las salidas
i_fecha = Gtk.Label(label="Fecha") 
i_nombre = Gtk.Label(label="Nombre")
i_grupo = Gtk.Label(label="Grupo")
i_beca = Gtk.Label(label="Beca")
i_uid = Gtk.Label(label="UID")
i_ne = Gtk.Label(label="NE")

# aplicar el estilo css al objeto
i_fecha.get_style_context().add_class("rejilla_item") 
i_nombre.get_style_context().add_class("rejilla_item")
i_grupo.get_style_context().add_class("rejilla_item")
i_beca.get_style_context().add_class("rejilla_item")
i_uid.get_style_context().add_class("rejilla_item")
i_ne.get_style_context().add_class("rejilla_item")

# alinear las etiquetas a la izquierda
i_fecha.set_xalign(-1.0)
i_nombre.set_xalign(-1.0)
i_grupo.set_xalign(-1.0)
i_beca.set_xalign(-1.0)
i_uid.set_xalign(-1.0)
i_ne.set_xalign(-1.0)

# Colocar etiquetas en la segunda columna (1) y filas correspondientes
rejilla.attach(i_fecha, 0, 1, 1, 1)
rejilla.attach(i_nombre, 1, 1, 1, 1)
rejilla.attach(i_grupo, 0, 2, 1, 1)
rejilla.attach(i_beca, 1, 2, 1, 1)
rejilla.attach(i_uid, 0, 3, 1, 1)
rejilla.attach(i_ne, 1, 3, 1, 1)

boton_imprimir = Gtk.Button.new_with_label("Limpiar datos") # crea un boton para limpiar los datos

rejilla.attach(boton_imprimir, 1, 0, 1, 1)  # Colocar el botón en la segunda columna y última fila

# Establecer el estilo CSS para la rejilla
css_provider = Gtk.CssProvider() # objeto que se utiliza para cargar y aplicar estilos css
css_provider.load_from_data(b'''
    .rejilla {
        background-color: #565869;
        padding: 6px 6px;
    }
    .rejilla_item {
        margin: 6px 6px;
        font-size: 14px;
        min-width: 400px;
    }
''')

screen = ventana.get_screen() # obtener el objeto screen
style_context = ventana.get_style_context() #obtener contexto de la pantalla principal
# se agrega el provedor de estilos css, osea estos estilos tendran prioridad
style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


def actualizar_info_interfaz(
        nombre,
        fecha,
        grupo,
        beca,
        uid,
        ne,
        ):
    # esta funcion permite actualizar las etiquetas desde la GUI
    gl.idle_add(i_nombre.set_text, f"Nombre: {nombre}")
    gl.idle_add(i_fecha.set_text, f"Fecha: {fecha}")
    gl.idle_add(i_grupo.set_text, f"Grupo: {grupo}")
    gl.idle_add(i_beca.set_text, f"Tipo de beca: {beca}")
    gl.idle_add(i_uid.set_text, f"UID de la tarjeta: {uid}")
    gl.idle_add(i_ne.set_text, f"Necesidades especiales de el/la alumno/a: {ne}")

def actualizar_datos():
    # valores predeterminados cuando no se a leído la tarjeta
    actualizar_info_interfaz(
        nombre = "Anónimo",
        fecha = 0,
        grupo = 0,
        beca = 0,
        uid = 0,
        ne = 0,
        )

    leer(funcion_salida=actualizar_info_interfaz)

def limpiar(widget):
    # valores cuando se limpia con el boton limpar
    actualizar_info_interfaz(
        nombre = "Anónimo",
        fecha = 0,
        grupo = 0,
        beca = 0,
        uid = 0,
        ne = 0,
        )

boton_imprimir.connect("clicked", limpiar) #ejecutar la funcion limpiar cuando el boton es presionado

def sigint_handler(signal, frame): # se ejecutara al recibir una señal de interruccupción
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler) # espera la señal de interrupción (Ctrl+C)

hilo = threading.Thread(target=actualizar_datos) # ejecutar función "actualizar_datos"
hilo.daemon = True  # El subproceso se detendrá cuando se cierre la ventana principal
hilo.start() # iniciar subproceso

ventana.show_all() # hace que los elementos en la ventana sean visibles
Gtk.main() # inicia el bucle principal de eventos, permite que la interfaz sea interactiva