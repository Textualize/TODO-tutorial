from textual.app import App
from textual.widgets import Button, Header, Input, Label


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Input(placeholder="Name:")
        yield Button("Submit")

    def on_button_pressed(self):
        name = self.query_one(Input).value
        self.mount(Label(name))


MyApp().run()
