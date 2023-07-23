from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class App(MDApp):
	def build(self):
		return MDLabel(
			text="CoreProject",
			halign="center"
		)

if __name__ == "__main__":
	App().run()