from textual.app import App
from textual.widgets import Label


class MyApp(App):
    CSS_PATH = "28_css.css"

    def compose(self):
        yield Label("This is some text!")


MyApp().run()
