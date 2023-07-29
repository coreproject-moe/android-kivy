from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

# import components
from libs.components.shared.appbar import appbar


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.md_bg_color = get_color_from_hex("#03020c")
        self.add_widget(appbar())
        carousel = Carousel(direction="right")
        for i in [
            "https://raw.githubusercontent.com/tokitou-san/CoreProject-V3-UI/4c44e794a89d8d0611eebb91d72fe6353f62c48f/static/images/characters/eliane/eliane.png",
            "https://raw.githubusercontent.com/tokitou-san/CoreProject-V3-UI/4c44e794a89d8d0611eebb91d72fe6353f62c48f/static/images/characters/eliane/eliane_2.png",
            "https://raw.githubusercontent.com/tokitou-san/CoreProject-V3-UI/4c44e794a89d8d0611eebb91d72fe6353f62c48f/static/images/characters/exy/exy.png",
            "https://raw.githubusercontent.com/tokitou-san/CoreProject-V3-UI/4c44e794a89d8d0611eebb91d72fe6353f62c48f/static/images/characters/futaba/futaba.png",
        ]:
            image = AsyncImage(source=i, fit_mode="contain")
            carousel.add_widget(image)
        self.add_widget(carousel)
