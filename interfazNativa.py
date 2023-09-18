#!/usr/bin/env python 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib as gl
import threading  # importa la biblioteca threading para trabajar con subprocesos
import signal # importa la biblioteca signal, modulo que permite trabajar con señales del sistema como Ctrl+C para interrumpir
import os # libreria para correr comandos bash dentro del codigo
from time import sleep

from lectorUID import leer

ventana = Gtk.Window(title="Lector de Tarjetas NFC") # iniciar una ventana
ventana.connect("destroy", Gtk.main_quit) # finalizar aplicación cuando se cierre la ventana
ventana.set_default_size(800, 600) # ajustar el tamaño de la ventana
ventana.maximize() # maximizarlo a tamaño completo

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) # agrega orientacion y espaciado
ventana.add(caja) # crea una caja en la ventana pricipal

label1 = Gtk.Label(label="Leea la tarjeta NFC en el lector") # Crear etiqueta de texto

i_fecha = Gtk.Label(label="Nombre") # Crear etiqueta de texto
i_nombre = Gtk.Label(label="Nombre") # Crear etiqueta de texto
i_grupo = Gtk.Label(label="Grupo") # Crear etiqueta de texto
i_beca = Gtk.Label(label="Beca") # Crear etiqueta de texto
i_uid = Gtk.Label(label="Salida de datos") # Crear etiqueta de texto
i_ne = Gtk.Label(label="Salida de datos") # Crear etiqueta de texto


boton_imprimir = Gtk.Button.new_with_label("Limpiar datos") # crear un boton 
caja.pack_start(label1, True, True, 0) # administración del espacio que cubre

caja.pack_start(i_fecha, True, True, 0) # 0 represanta el espacio entre widgets  
caja.pack_start(i_nombre, True, True, 0) # 0 represanta el espacio entre widgets  
caja.pack_start(i_grupo, True, True, 0) # 0 represanta el espacio entre widgets  
caja.pack_start(i_beca, True, True, 0) # 0 represanta el espacio entre widgets  
caja.pack_start(i_uid, True, True, 0) # 0 represanta el espacio entre widgets  
caja.pack_start(i_ne, True, True, 0) # 0 represanta el espacio entre widgets  

caja.pack_start(boton_imprimir, True, True, 0) # Agrega el boton a la caja

def actualizar_info_interfaz(
        nombre,
        fecha,
        grupo,
        beca,
        uid,
        ne,
        ):
    gl.idle_add(i_nombre.set_text, f"Nombre: {nombre}")
    gl.idle_add(i_fecha.set_text, f"Fecha: {fecha}")
    gl.idle_add(i_grupo.set_text, f"Grupo: {grupo}")
    gl.idle_add(i_beca.set_text, f"Tipo de beca: {beca}")
    gl.idle_add(i_uid.set_text, f"UID de la tarjeta: {uid}")
    gl.idle_add(i_ne.set_text, f"Necesidades especiales de el/la alumno/a: {ne}")

def actualizar_datos():
    #while True:
    #    card_data = leer()  # Llama a la función leer para obtener los datos
    # Actualiza el texto en la etiqueta label2 (o cualquier otro widget) con card_data
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
    actualizar_info_interfaz(
        nombre = "Anónimo",
        fecha = 0,
        grupo = 0,
        beca = 0,
        uid = 0,
        ne = 0,
        )

boton_imprimir.connect("clicked", limpiar)

def sigint_handler(signal, frame): # se ejecutara al recibir una señal de interruccupción
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler) # espera la señal de interrupción (Ctrl+C)

hilo = threading.Thread(target=actualizar_datos) # ejecutar función "actualizar_datos"
hilo.daemon = True  # El subproceso se detendrá cuando se cierre la ventana principal
hilo.start() # iniciar subproceso

ventana.show_all() # hace que los elempentos en la ventana sean visibles
Gtk.main() # inicia el bucle principal de eventos, permite que la interfaz sea interactiva