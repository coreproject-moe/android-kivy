from kivymd.uix.screen import MDScreen

from android.geckoview import get_url

# import components


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        get_url("https://google.com")

        # self.md_bg_color = get_color_from_hex("#03020c")
        # self.add_widget(AppBar())
