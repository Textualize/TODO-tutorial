from textual.app import App
from textual.widgets import Label


class MyApp(App):
    CSS_PATH = "29_css.css"

    def compose(self):
        yield Label("Plain.")
        yield Label("With a class", classes="blue_bg")
        yield Label("With an id", classes="blue_bg", id="label")


MyApp().run()
