from textual.app import App
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button


class Deletable(Widget):
    class DeletionRequest(Message):
        def __init__(self, to_delete):
            super().__init__()
            self.to_delete = to_delete

    def compose(self):
        yield Button("Delete me.")

    def on_button_pressed(self):
        self.post_message(Deletable.DeletionRequest(self))


class MyApp(App):
    def compose(self):
        yield Deletable()

    def on_deletable_deletion_request(self, message):
        message.to_delete.remove()


MyApp().run()
