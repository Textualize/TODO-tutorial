from textual.app import App
from textual.widgets import Button, Header, Input, Label


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Label("Name:")
        yield Input(placeholder="name")
        yield Label("Surname:")
        yield Input(placeholder="surname")
        yield Label("Email:")
        yield Input(placeholder="email")

        yield Button("Click me!")


MyApp().run()
