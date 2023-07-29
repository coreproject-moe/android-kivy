import pytest
from kivy.tests.common import GraphicUnitTest
from kivy.config import Config
from main import MainApp


class TestApp(GraphicUnitTest):
    def setUp(self):
        # Set the desired window size for testing
        Config.set("graphics", "width", 360)
        Config.set("graphics", "height", 640)
        super(TestApp, self).setUp()

    def test_screen_size(self):
        app = MainApp()
        app.run()

        # Assert that the app's window size matches the configured size
        self.assertEqual(app.window.size, (360, 640))

        # You can also check other elements on the screen, if needed
        # For example:
        home_screen = app.root
        self.assertEqual(home_screen.width, 360)
        self.assertEqual(home_screen.height, 640)
