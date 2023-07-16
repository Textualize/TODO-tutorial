# import time

from textual import work
from textual.app import App
from textual.widgets import Label


class MyApp(App):
    def on_mount(self):
        self.load_data()

    @work
    def load_data(self):
        with open("path/to/data", "r") as f:
            for line in f:
                # time.sleep(2)
                self.call_from_thread(self.mount, Label(line.strip()))


MyApp().run()
