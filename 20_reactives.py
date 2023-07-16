from textual.app import App
from textual.reactive import reactive
from textual.widgets import Button, Label


class MyApp(App):
    counter = reactive(0)

    def __init__(self):
        self.label = Label()
        super().__init__()

    def compose(self):
        yield self.label
        yield Button("+1")

    def on_button_pressed(self):
        self.counter += 1

    def watch_counter(self):
        self.label.update(str(self.counter))


MyApp().run()
