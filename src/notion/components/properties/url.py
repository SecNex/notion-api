from .property import Property

class Url(Property):
    def __init__(self, name: str, url: str, id: str = None, type: str = "url") -> None:
        super().__init__()
        self.name = name
        self.url = url
        self.id = id
        self.type = type