from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__

class MotoApp(App):

    def build(self):
        return MyRoot()

app = MotoApp()
app.run()