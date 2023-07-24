from kivy import Config
# config window size
Config.set("graphics", "width", 360)
Config.set("graphics", "height", 640)

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="CoreProject", halign="center")

if __name__ == "__main__":
    MainApp().run()