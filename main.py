from kivy import Config
# config window size
Config.set("graphics", "width", 360)

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="CoreProject", halign="center")


MainApp().run()