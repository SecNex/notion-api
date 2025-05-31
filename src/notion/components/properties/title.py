from .property import Property

class Title(Property):
    def __init__(self, name: str, title: str, id: str = None, type: str = "title") -> None:
        super().__init__()
        self.name = name
        self.title = title[0]["plain_text"]
        self.id = id
        self.type = type