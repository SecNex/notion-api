from .property import Property

class Checkbox(Property):
    def __init__(self, name: str, checkbox: bool, id: str = None, type: str = "checkbox") -> None:
        super().__init__()
        self.name = name
        self.checkbox = checkbox
        self.id = id
        self.type = type