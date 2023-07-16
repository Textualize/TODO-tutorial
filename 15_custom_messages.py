from textual.app import App
from textual.message import Message
from textual.widgets import Button


class Ring(Message):
    pass


class MyApp(App):
    def compose(self):
        yield Button("Ring")

    def on_button_pressed(self):
        self.post_message(Ring())

    def on_ring(self):
        self.bell()


MyApp().run()
