from functools import partial

from textual import on
from textual.app import App
from textual.containers import Horizontal
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
        self.description_input = Input(placeholder="description")
        self.date_input = Input(placeholder="date")
        yield Label("Description:")
        yield self.description_input
        yield Label("Date:")
        yield self.date_input
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
        self.description_label = Label()
        self.date_label = Label()

    def compose(self):
        with Horizontal():
            yield Button("Delete", id="delete")
            yield Button("Edit", id="edit")
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

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def action_new_item(self):
        self.push_screen(TodoItemDetailsScreen(), self.new_item_callback)

    def new_item_callback(self, data):
        item = TodoItem()
        description, date = data
        item.description = description
        item.date = date
        self.mount(item)

    def edit_item_callback(self, item, data):
        description, date = data
        item.description = description
        item.date = date

    def on_todo_item_delete(self, message):
        message.item.remove()

    def on_todo_item_edit(self, message):
        self.push_screen(
            TodoItemDetailsScreen(), partial(self.edit_item_callback, message.item)
        )


TodoApp().run()
