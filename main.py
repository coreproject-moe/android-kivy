from kivy import Config
from kivy.config import platform

if platform != "android":
    # config window size
    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 640)

# MdTool overrides the config

from libs.screens.home_screen import HomeScreen  # noqa: E402
from kivymd.tools.hotreload.app import MDApp  # noqa: E402


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):
        return HomeScreen()


if __name__ == "__main__":
    MainApp().run()
