from __future__ import annotations

from dataclasses import dataclass

from textual.app import App
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Checkbox, Header, Footer, Label


class TodoItem(Widget):
    @dataclass
    class Done(Message):
        item: TodoItem

    def compose(self):
        yield Checkbox()
        yield Label("Item", id="description")
        yield Label("dd-mm-yyyy", id="date")

    def on_checkbox_changed(self, event):
        event.stop()
        self.post_message(TodoItem.Done(self))


class TodoApp(App):
    BINDINGS = [("a", "add_todo", "Add item")]
    CSS_PATH = "todo_first.css"

    def compose(self):
        yield Header()
        yield TodoItem()
        yield Footer()

    def action_add_todo(self):
        self.mount(TodoItem())

    def on_todo_item_done(self, event):
        event.item.remove()


if __name__ == "__main__":
    TodoApp().run()
