from .property import Property

class Number(Property):
    def __init__(self, name: str, id: str = None, type: str = "number", number: float = None) -> None:
        super().__init__()
        self.name = name
        self.id = id
        self.type = type
        self.number = number