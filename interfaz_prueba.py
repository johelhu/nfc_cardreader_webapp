import kivy #Libreria de kive
from kivy.app import App #Lugar para vaciar los widgets
from kivy.uix.boxlayout import BoxLayout # Forma en la que se va a ver
from kivy.config import Config #Poder hacer configuraciones
#Config.set('graphics', 'width', 400 #configurar el alto de la ventana
#Config.set('graphics', 'height', 400 #configurar altura de la ventana

class Box01(BoxLayout): #Declaración de nuestro Widget
    None #Accion a realizar en este caso ninguna
    
class MainApp(App): #Llamar a nuestro archivo .kv (main.kv) para darle las apariencias a los widgets
    title = "Hola Mundo" #Nombre de la aplicacion
    def build(self): #Lo primero que busca kiby para saber que hacer
        return Box01() #Le decimos que nos regrese (Contenedor_01)
        
if __name__== '__main__': #Condición para ejecutar
    MainApp().run() #Correr la aplicación

#class FirstApp(App):
#    def build(self):
#        return Label(text = "prueba using name/main")
#
#if __name__== "__main__":
#    FirstApp().run()
