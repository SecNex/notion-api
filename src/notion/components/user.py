class User:
    def __init__(self, object: str, id: str, name: str, avatar_url: str, type: str = None, person: dict = {}) -> None:
        self.object = object
        self.id = id
        self.name = name
        self.avatar_url = avatar_url
        self.type = type
        self.person = person