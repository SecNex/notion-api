from .property import Property

class DateProperty:
    def __init__(self, start: str, end: str, time_zone: str = None) -> None:
        self.start = start
        self.end = end
        self.time_zone = time_zone

class Date(Property):
    def __init__(self, name: str, date: dict, id: str = None, type: str = "date") -> None:
        super().__init__()
        self.name = name
        self.date = DateProperty(**date)
        self.id = id
        self.type = type