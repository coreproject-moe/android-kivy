from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton


class AppBar:
    def create_appbar(self):
        # global variables
        empty_space = Widget()

        # Appbar elements
        app_bar_layout = MDBoxLayout(
            size_hint_y=None,
            height="50dp",
            pos_hint={"top": 1},
            padding="10dp",
            orientation="horizontal"
        )
        # CoreProject logo
        core_logo = MDFillRoundFlatButton(
            text="Logo",
            pos_hint={"x": 0, "top": 1}
        )
        # Right side elements
        appbar_right = MDBoxLayout(
            orientation="horizontal",
            spacing="5dp"
        )
        # Search button
        search_button = MDFillRoundFlatIconButton(
            text="Search",
            pos_hint={"x": 0, "top": 1}
        )
        # Notification button
        notification_button = MDFillRoundFlatButton(
            text="Noti",
            pos_hint={"x": 0, "top": 1}
        )
        # Profile button
        profile_button = MDFillRoundFlatButton(
            text="Tokito",
            pos_hint={"x": 0, "top": 1}
        )
        # Add an empty Widget for aligning items left and right
        appbar_right.add_widget(empty_space)
        # Add other widgets
        appbar_right.add_widget(search_button)
        appbar_right.add_widget(notification_button)
        appbar_right.add_widget(profile_button)
        # Add widgets to the main Appbar layout
        app_bar_layout.add_widget(core_logo)
        app_bar_layout.add_widget(appbar_right)

        return app_bar_layout
