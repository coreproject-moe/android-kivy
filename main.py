from kivy import Config
# config window size
Config.set("graphics", "width", 360)
Config.set("graphics", "height", 640)

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):

        self.theme_cls.theme_style = "Dark"
        return MDLabel(text="CoreProject", halign="center")

if __name__ == "__main__":
    MainApp().run()