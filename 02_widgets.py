from textual.app import App
from textual.widgets import Button, Header


class MyApp(App):
    def compose(self):
        yield Header()
        yield Button()


MyApp().run()
