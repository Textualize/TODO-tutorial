from __future__ import annotations

from dataclasses import dataclass
import datetime as dt
from functools import partial
import json

from textual import on, work
from textual.app import App
from textual.containers import Container, Center
from textual.message import Message
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widget import Widget
from textual.widgets import Button, Header, Footer, Label, Input


class TodoItem(Widget):
    @dataclass
    class Done(Message):
        item: TodoItem

    @dataclass
    class Edit(Message):
        item: TodoItem

    description = reactive("", init=False)
    date = reactive("", init=False)

    def __init__(self, description, date):
        super().__init__()
        self.description_label = Label(id="description")
        self.date_label = Label(id="date")
        self.description = description
        self.date = date

    def watch_description(self, value):
        self.description_label.update(value)

    def watch_date(self, value):
        self.date_label.update(value)

    def compose(self):
        yield Button("✅", classes="emoji-button", id="done")
        yield Button("📝", classes="emoji-button", id="edit")
        yield self.description_label
        yield self.date_label

    @on(Button.Pressed, "#done")
    def remove_item_done(self, event):
        event.stop()
        self.post_message(TodoItem.Done(self))

    @on(Button.Pressed, "#edit")
    def edit_item(self, event):
        event.stop()
        self.post_message(TodoItem.Edit(self))


class ItemScreenDetails(ModalScreen):
    def __init__(self, default_description="", default_date=""):
        self.default_description = default_description
        self.default_date = default_date
        super().__init__()

    def compose(self):
        with Container():
            yield Label("Type description and due date in the format dd/mm/yyyy.")
            yield Input(
                self.default_description, placeholder="Description", id="description"
            )
            yield Input(self.default_date, placeholder="Due date dd/mm/yyyy", id="date")
            with Center():
                yield Button("Submit")

    def on_input_submitted(self):
        self.focus_next()

    def on_button_pressed(self):
        description = self.query_one("#description").value
        if not description:
            self.app.bell()
            self.query_one("#description").focus()
            return

        date = self.query_one("#date").value
        try:
            dt.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            self.app.bell()
            self.query_one("#date").focus()
            return

        self.dismiss((description, date))


class TodoApp(App):
    BINDINGS = [("a", "add_todo", "Add item")]
    CSS_PATH = "todo_third.css"

    def compose(self):
        yield Header()
        yield Footer()

    def on_mount(self):
        self.load_data()

    def new_item(self, values):
        description, date = values
        self.screen.mount(TodoItem(description, date))
        self.save_data()

    def edit_item(self, item, values):
        item.description, item.date = values
        self.save_data()

    def action_add_todo(self):
        self.push_screen(ItemScreenDetails(), self.new_item)

    def on_todo_item_done(self, event):
        event.item.remove()
        self.save_data()

    def on_todo_item_edit(self, event):
        item = event.item
        self.push_screen(
            ItemScreenDetails(item.description, item.date),
            partial(self.edit_item, item),
        )

    @work
    def load_data(self):
        with open("data.json", "r") as f:
            loaded = json.load(f)
        for values in loaded:
            item = TodoItem(*values)
            self.call_from_thread(self.mount, item)

    @work
    def save_data(self):
        to_dump = [(item.description, item.date) for item in self.query(TodoItem)]
        with open("data.json", "w") as f:
            json.dump(to_dump, f, indent=4)


if __name__ == "__main__":
    TodoApp().run()
