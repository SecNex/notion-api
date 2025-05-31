from .property import Property

class Email(Property):
    def __init__(self, name: str, email: str, id: str = None, type: str = "email") -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.id = id
        self.type = type