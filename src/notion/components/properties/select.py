from .property import Property

class SelectOption:
    def __init__(self, id: str, name: str, color: str = "default") -> None:
        self.id = id
        self.name = name
        self.color = color
    
class MulitSelect:
    def __init__(self, name: str, multi_select: list[SelectOption], id: str = None, type: str = "multi_select") -> None:
        super().__init__()
        self.name = name
        self.id = id
        self.multi_select = [SelectOption(**option) for option in multi_select]
        self.type = type

class Select(Property):
    def __init__(self, name: str, select: dict, id: str = None, type: str = "select") -> None:
        super().__init__()
        self.name = name
        self.id = id
        self.select = SelectOption(**select)
        self.type = type