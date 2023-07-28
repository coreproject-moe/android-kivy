from kivy import Config
# config window size
Config.set("graphics", "width", 360)
Config.set("graphics", "height", 640)

from kivymd.tools.hotreload.app import MDApp
# import screens
from libs.screens.home_screen import HomeScreen

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):
        return HomeScreen()

if __name__ == "__main__":
    MainApp().run()
