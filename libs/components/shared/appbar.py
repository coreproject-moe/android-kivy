from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
)

class AppBar(MDRelativeLayout):
    def __init__(self, *args, **kwargs) -> None:
        super(AppBar, self).__init__(*args, **kwargs)

        self.size_hint_y = 0.1
        self.pos_hint = {"top": 1}
        # Add widgets
        self.add_widget(self._create_logo())
        self.add_widget(self._create_right_section())

    def _create_logo(self) -> MDFillRoundFlatButton:
        # CoreProject logo
        return MDFillRoundFlatButton(
            text="Logo",
            pos_hint={
                "center_y": 0.5,
                "x": 0.035,
            },
        )

    def _create_right_section(self) -> MDBoxLayout:
        # Buttons
        appbar_buttons = {
            "search_button": MDFillRoundFlatIconButton(
                text="Search",
                pos_hint={
                    "center_y": 0.5,
                },
            ),
            "notification_button": MDFillRoundFlatButton(
                text="Noti",
                pos_hint={
                    "center_y": 0.5,
                },
            ),
            "profile_button": MDFillRoundFlatButton(
                text="Tokito",
                pos_hint={
                    "center_y": 0.5,
                },
            ),
        }
        # Right side container
        appbar_right = MDBoxLayout(
            orientation="horizontal",
            spacing="5dp",
            pos_hint={
                "right": 0.96,
            },
            size_hint_x=None,
            width="228dp",
        )
        # Add widgets to `appbar_right`
        for button in appbar_buttons.values():
            appbar_right.add_widget(button)

        return appbar_right