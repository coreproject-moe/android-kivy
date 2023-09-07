from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

# import components
from libs.components.shared.appbar import AppBar


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.md_bg_color = get_color_from_hex("#03020c")
        self.add_widget(AppBar())
