from textual.app import App
from textual.widget import Widget
from textual.widgets import Input, Label


class LabelledInput(Widget):
    def compose(self):
        yield Label("My label!")
        yield Input()


class MyApp(App):
    def compose(self):
        yield LabelledInput()


MyApp().run()
