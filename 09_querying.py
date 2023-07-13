from textual.app import App
from textual.widgets import Button, Header, Input


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Input(placeholder="Name:")
        yield Button("Submit")

    def on_button_pressed(self):
        input_widget = self.query(Input).first()
        input_value = input_widget.value
        self.exit(input_value)


print(MyApp().run())
