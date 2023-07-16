from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Label


class MyApp(App):
    def compose(self):
        yield Label("first label!")
        with Horizontal():
            yield Label("second label.")
            yield Label("third label...")


MyApp().run()
