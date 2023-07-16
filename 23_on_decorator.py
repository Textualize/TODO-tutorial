from textual import on
from textual.app import App
from textual.reactive import reactive
from textual.widgets import Button, Label


class MyApp(App):
    counter = reactive(0)

    def compose(self):
        self.label = Label()
        yield self.label
        yield Button("+1", id="one")
        yield Button("+10", id="ten")
        yield Button("+100", id="hundred")

    @on(Button.Pressed, "#one")
    def plus_one(self):
        self.counter += 1

    @on(Button.Pressed, "#ten")
    def plus_ten(self):
        self.counter += 10

    @on(Button.Pressed, "#hundred")
    def plus_hundred(self):
        self.counter += 100

    def watch_counter(self):
        self.label.update(str(self.counter))


MyApp().run()
