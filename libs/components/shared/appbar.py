from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
)


class AppBar(MDBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.padding = 10
        self.spacing = 5
        self.pos_hint = {"top": 1}
        # Add widgets
        self.add_widget(self._build_logo_())
        self.add_widget(self._build_right_section_())

    def _build_logo_(self) -> MDFillRoundFlatButton:
        # CoreProject logo
        return MDFillRoundFlatButton(text="Logo")

    def _build_right_section_(self) -> MDRelativeLayout:
        appbar_right = MDRelativeLayout()
        # Buttons mapping
        appbar_buttons = {
            "search_button": MDFillRoundFlatIconButton(text="Search"),
            "notification_button": MDFillRoundFlatButton(text="Noti"),
            "profile_button": MDFillRoundFlatButton(text="Tokito"),
        }
        # Buttons container
        buttons_layout = MDBoxLayout(adaptive_size=True, spacing=5, pos_hint={"right": 1})
        # Add widgets to `appbar_right`
        for button in appbar_buttons.values():
            buttons_layout.add_widget(button)
        # Add buttons_layout to main layout
        appbar_right.add_widget(buttons_layout)

        return appbar_right
