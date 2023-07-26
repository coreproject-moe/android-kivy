from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from libs.components.app_bar import AppBar

class HomePage(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.md_bg_color = get_color_from_hex("#03020c")
        self.add_widget(AppBar.create_appbar(self))
