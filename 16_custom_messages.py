from textual.message import Message
from textual.widget import Widget


class RingerWidget(Widget):
    class Ring(Message):
        pass
