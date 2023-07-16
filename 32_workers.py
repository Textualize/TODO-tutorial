# import time

from textual.app import App
from textual.widgets import Button, Input, Label


class MyApp(App):
    def compose(self):
        yield Input(placeholder="filepath")
        yield Button("Load!")

    def on_button_pressed(self):
        filepath = self.query_one(Input).value
        self.load_data(filepath)

    def load_data(self, filepath):
        with open(filepath, "r") as f:
            for line in f:
                # time.sleep(2)
                self.mount(Label(line.strip()))


MyApp().run()
