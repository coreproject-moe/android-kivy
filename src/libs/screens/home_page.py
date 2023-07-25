from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.utils import get_color_from_hex

class HomePage(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_widget(self.layout())
        self.md_bg_color = get_color_from_hex("#03020c")

    def layout(self):
        app_bar_layout = MDRelativeLayout(
            size_hint_y = None,
            height = "50dp",
            pos_hint = {"top": 1}
        )

        button = MDFillRoundFlatButton(
            text="Logo",
            pos_hint={"x": 0, "top": 1}
        )
        app_bar_layout.add_widget(button)

        return app_bar_layout