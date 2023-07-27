from kivy import Config
from libs.screens.home_page import HomePage
from kivymd.tools.hotreload.app import MDApp


# config window size
Config.set("graphics", "width", 360)
Config.set("graphics", "height", 640)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):
        return HomePage()


if __name__ == "__main__":
    MainApp().run()
