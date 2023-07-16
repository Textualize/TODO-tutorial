from textual.app import App
from textual.widget import Widget
from textual.widgets import Footer, Header, Label


class TodoItem(Widget):
    DEFAULT_CSS = """
    TodoItem {
        height: 2;
    }
    """

    def compose(self):
        yield Label("I should get this done!")
        yield Label("dd/mm/yyyy")


class TodoApp(App):
    BINDINGS = [("n", "new_item", "New")]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def action_new_item(self):
        self.mount(TodoItem())


TodoApp().run()
