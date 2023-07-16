from textual.app import App
from textual.widget import Widget
from textual.widgets import Button, Header, Input, Label


class LabelledInput(Widget):
    DEFAULT_CSS = """
    LabelledInput {
        height: 4;
    }
    """

    def compose(self):
        yield Label("Label:")
        yield Input(placeholder="label")


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield LabelledInput()
        yield Button("Click me!")


MyApp().run()
