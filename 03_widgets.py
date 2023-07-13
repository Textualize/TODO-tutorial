from textual.app import App
from textual.widgets import Button, Header


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Button("Click me!")


MyApp().run()
