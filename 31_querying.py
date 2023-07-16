from textual.app import App
from textual.widgets import Button, Header, Input, Label


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Input(placeholder="Name:")
        yield Input(placeholder="Surname:")
        yield Button("Submit")

    def on_button_pressed(self):
        data = " ".join(input.value for input in self.query(Input))
        self.mount(Label(data))


MyApp().run()
