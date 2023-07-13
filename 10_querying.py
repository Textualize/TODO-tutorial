from textual.app import App
from textual.widgets import Button, Header, Input


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Input(placeholder="Name:")
        yield Input(placeholder="Surname:")
        yield Input(placeholder="Email:")
        yield Button("Submit")

    def on_button_pressed(self):
        values = [input.value for input in self.query(Input)]
        self.exit(values)


print(MyApp().run())
