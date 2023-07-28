from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen

# import components
from libs.components.appbar import appbar


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.md_bg_color = get_color_from_hex("#03020c")
        self.add_widget(appbar())
