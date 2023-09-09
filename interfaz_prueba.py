import kivy
from kivy.app import App
from kivy.uix.label import Label

class FirstApp(App):
    def build(self):
        return Label(text = "prueba using name/main")

if __name__== "__main__":
    FirstApp().run()
