from textual.app import App
from textual.widgets import Button


class MyApp(App):
    def compose(self):
        yield Button("Ring")

    def on_button_pressed(self):
        self.bell()


MyApp().run()
