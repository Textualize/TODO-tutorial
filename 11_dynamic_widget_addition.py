from textual.app import App
from textual.widgets import Footer, Label


class MyApp(App):
    BINDINGS = [("b", "bell", "Ring")]

    def compose(self):
        yield Footer()

    def action_bell(self):
        self.bell()
        self.mount(Label("Ring!"))


MyApp().run()
