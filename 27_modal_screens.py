import time

from textual.app import App
from textual.screen import ModalScreen
from textual.widgets import Button, Label


class MyModalScreen(ModalScreen):
    DEFAULT_CSS = """
    MyModalScreen {
        align: center middle;
    }
    """

    def compose(self):
        yield Label("My modal screen")
        yield Button("Exit")

    def on_button_pressed(self):
        self.dismiss(time.time())


class MyApp(App):
    def compose(self):
        yield Button("Push modal!")

    def on_button_pressed(self):
        self.push_screen(MyModalScreen(), self.modal_screen_callback)

    def modal_screen_callback(self, time):
        self.mount(Label(f"Modal dismissed at {time}."))


MyApp().run()
