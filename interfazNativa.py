#!/usr/bin/env python 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import threading  # importa la biblioteca threading para trabajar con subprocesos
import signal # importa la biblioteca signal, modulo que permite trabajar con señales del sistema como Ctrl+C para interrumpir
import os # libreria para correr comandos bash dentro del codigo

from lectorUID import leer

ventana = Gtk.Window(title="Lector de Tarjetas NFC") # iniciar una ventana
ventana.connect("destroy", Gtk.main_quit) # finalizar aplicación cuando se cierre la ventana
ventana.set_default_size(800, 600) # ajustar el tamaño de la ventana
ventana.maximize() # maximizarlo a tamaño completo

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) # agrega orientacion y espaciado
ventana.add(caja) # crea una caja en la ventana pricipal

label1 = Gtk.Label(label="Leea la tarjeta NFC en el lector") # Creear etiqueta de texto
label2 = Gtk.Label(label="Salida de datos") # el primer true es lo horizontal, el segundo lo vertical
caja.pack_start(label1, True, True, 0) # administración del espacio que cubre
caja.pack_start(label2, True, True, 0) # 0 represanta el espacio entre widgets      

def actualizar_datos():
    while True:
        resultado = leer()  # Llama a la función leer para obtener los datos
        label2.set_text(resultado)  # Actualiza el texto en la etiqueta label2

def sigint_handler(signal, frame): # se ejecutara al recibir una señal de interruccupción
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler) # espera la señal de interrupción (Ctrl+C)

hilo = threading.Thread(target=actualizar_datos) # ejecutar función "actualizar_datos"
hilo.daemon = True  # El subproceso se detendrá cuando se cierre la ventana principal
hilo.start() # iniciar subproceso

ventana.show_all() # hace que los elempentos en la ventana sean visibles
Gtk.main() # inicia el buble principal de eventos, permite que la interfaz sea interactiva