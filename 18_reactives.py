from textual.app import App
from textual.reactive import reactive
from textual.widgets import Button


class MyApp(App):
    counter = reactive(0)

    def compose(self):
        yield Button("+1")

    def on_button_pressed(self):
        self.counter += 1

    def watch_counter(self):
        self.bell()


MyApp().run()
