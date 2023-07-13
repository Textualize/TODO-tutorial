from textual.app import App
from textual.widgets import Button, Header, Input


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Button("Click me!")
        yield Input(placeholder="Name:")


MyApp().run()
