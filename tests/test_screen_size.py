import pytest
from kivy.tests.common import GraphicUnitTest
from kivy.config import Config
from main import MainApp


class TestApp(GraphicUnitTest):
    def test_screen_size(self):
        app = MainApp()
        app.run()

        # Assert that our configs are okay
        self.assertEqual(app.root.width, 360)
        self.assertEqual(app.root.height, 640)
