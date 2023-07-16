from textual.app import App


class MyApp(App):
    BINDINGS = [("b", "bell")]

    def action_bell(self):
        self.bell()


MyApp().run()
