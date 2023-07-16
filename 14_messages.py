from textual.app import App
from textual.widgets import Button, Input


class MyApp(App):
    def compose(self):
        yield Button("Ring")
        yield Input()

    def on_button_pressed(self):
        self.bell()

    def on_input_changed(self):
        self.bell()


MyApp().run()
