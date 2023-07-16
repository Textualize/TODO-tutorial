from textual import on
from textual.app import App
from textual.reactive import reactive
from textual.widgets import Button, Label


class MyApp(App):
    counter = reactive(0)

    def compose(self):
        self.label = Label()
        yield self.label
        yield Button("+1")
        yield Button("+10")
        yield Button("+100")

    @on(Button.Pressed)
    def increment_counter(self):
        self.counter += 1

    def watch_counter(self):
        self.label.update(str(self.counter))


MyApp().run()
