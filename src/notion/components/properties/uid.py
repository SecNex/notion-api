from .property import Property

class UniqueIdProperty:
    def __init__(self, number: int, prefix: str) -> None:
        self.number = number
        self.prefix = prefix

class UniqueId(Property):
    def __init__(self, name: str, unique_id: str, id: str = None, type: str = "unique_id") -> None:
        super().__init__()
        self.name = name
        self.unique_id = UniqueIdProperty(**unique_id)
        self.id = id
        self.type = type