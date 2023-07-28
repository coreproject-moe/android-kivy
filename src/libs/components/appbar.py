from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
)

def appbar() -> MDRelativeLayout:
    # Appbar elements
    app_bar_layout = MDRelativeLayout(
        size_hint_y=0.1,
        pos_hint={
            "top": 1,
        },
    )
    # CoreProject logo
    core_logo = MDFillRoundFlatButton(
        text="Logo",
        pos_hint={
            "center_y": 0.5,
            "x": 0.035,
        },
    )

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
    # Right side elements
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

    # Add widgets to the main Appbar layout
    app_bar_layout.add_widget(core_logo)
    app_bar_layout.add_widget(appbar_right)

    return app_bar_layout