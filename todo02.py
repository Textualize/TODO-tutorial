from textual.app import App
from textual.widgets import Header


class TodoApp(App):
    TITLE = "TODO Manager"

    def compose(self):
        yield Header()


if __name__ == "__main__":
    TodoApp().run()
