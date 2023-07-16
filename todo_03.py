from functools import partial
import json

from textual import on, work
from textual.app import App
from textual.containers import Center, Container, Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widget import Widget
from textual.widgets import Button, Footer, Header, Input, Label


class TodoItemDetailsScreen(ModalScreen):
    DEFAULT_CSS = """
    TodoItemDetailsScreen {
        align: center middle;
    }
    """

    def compose(self):
        self.description_input = Input(placeholder="Description")
        self.date_input = Input(placeholder="Due date dd/mm/yyyy")
        with Container():
            yield Label("Type description and due date in the format dd/mm/yyyy.")
            yield self.description_input
            yield self.date_input
            with Center():
                yield Button("Submit")

    def on_button_pressed(self):
        data = (self.description_input.value, self.date_input.value)
        self.dismiss(data)


class TodoItem(Widget):
    DEFAULT_CSS = """
    TodoItem {
        height: 2;
    }
    """

    description = reactive("")
    date = reactive("")

    class Edit(Message):
        def __init__(self, item):
            super().__init__()
            self.item = item

    class Delete(Message):
        def __init__(self, item):
            super().__init__()
            self.item = item

    def __init__(self):
        super().__init__()
        self.description_label = Label(id="description")
        self.date_label = Label(id="date")

    def compose(self):
        with Horizontal():
            yield Button("✅", classes="emoji-button", id="delete")
            yield Button("📝", classes="emoji-button", id="edit")
            yield self.description_label
            yield self.date_label

    def watch_description(self, description):
        self.description_label.update(description)

    def watch_date(self, date):
        self.date_label.update(date)

    @on(Button.Pressed, "#edit")
    def edit_request(self):
        self.post_message(self.Edit(self))

    @on(Button.Pressed, "#delete")
    def delete_request(self):
        self.post_message(self.Delete(self))


class TodoApp(App):
    BINDINGS = [("n", "new_item", "New")]

    CSS_PATH = "todo.css"

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self):
        self.load_data()

    def action_new_item(self):
        self.push_screen(TodoItemDetailsScreen(), self.new_item_callback)

    def new_item_callback(self, data):
        item = TodoItem()
        description, date = data
        item.description = description
        item.date = date
        self.mount(item)
        self.save_data()

    def edit_item_callback(self, item, data):
        description, date = data
        item.description = description
        item.date = date
        self.save_data()

    def on_todo_item_delete(self, message):
        message.item.remove()
        self.save_data()

    def on_todo_item_edit(self, message):
        self.push_screen(
            TodoItemDetailsScreen(), partial(self.edit_item_callback, message.item)
        )

    @work
    def save_data(self):
        to_dump = [(item.description, item.date) for item in self.query(TodoItem)]
        with open("data.json", "w") as f:
            json.dump(to_dump, f, indent=4)

    @work
    def load_data(self):
        with open("data.json", "r") as f:
            loaded = json.load(f)
        for description, date in loaded:
            item = TodoItem()
            item.description = description
            item.date = date
            self.call_from_thread(self.mount, item)


TodoApp().run()
