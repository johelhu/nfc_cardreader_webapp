import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Función para buscar la UID en la base de datos
def buscar_uid(widget):
    uid_buscar = entry.get_text()
    if uid_buscar in base_de_datos:
        resultado_label.set_text(f"UID encontrada en la base de datos. Datos relacionados: {base_de_datos[uid_buscar]}")
    else:
        resultado_label.set_text("UID no encontrada en la base de datos")

# Base de datos ficticia (puedes reemplazarla con tus propios datos)
base_de_datos = {
    "UID1": "Datos relacionados 1",
    "UID2": "Datos relacionados 2",
    "UID3": "Datos relacionados 3"
}

# Crear la ventana principal
ventana = Gtk.Window(title="Lector de Tarjetas NFC")
ventana.connect("destroy", Gtk.main_quit)

# Crear una caja de diseño vertical
caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
ventana.add(caja)

# Crear una etiqueta y un cuadro de entrada de texto
label = Gtk.Label(label="Ingresa la UID de la tarjeta NFC:")
entry = Gtk.Entry()
caja.pack_start(label, True, True, 0)
caja.pack_start(entry, True, True, 0)

# Crear un botón para buscar la UID en la base de datos
boton_buscar = Gtk.Button(label="Buscar UID")
boton_buscar.connect("clicked", buscar_uid)
caja.pack_start(boton_buscar, True, True, 0)

# Crear una etiqueta para mostrar el resultado
resultado_label = Gtk.Label(label="")
caja.pack_start(resultado_label, True, True, 0)

# Mostrar la ventana
ventana.show_all()

# Iniciar la aplicación GTK
Gtk.main()
