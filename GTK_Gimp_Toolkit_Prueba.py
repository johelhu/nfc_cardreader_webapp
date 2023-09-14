import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Mi Aplicación GTK")

        # Crear un botón
        boton = Gtk.Button(label="¡Haz clic en mí!")
        boton.connect("clicked", self.on_button_clicked)
        self.add(boton)

    def on_button_clicked(self, widget):
        print("¡Botón clickeado!")

win = MiVentana()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

