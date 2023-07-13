from textual.app import App
from textual.widget import Widget
from textual.widgets import Input, Label


class LabelledInput(Widget):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self):
        yield Label(f"{self.label}:")
        yield Input(placeholder=self.label.lower())


class MyApp(App):
    def compose(self):
        yield LabelledInput("Name")


MyApp().run()
