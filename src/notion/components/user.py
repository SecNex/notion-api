class User:
    def __init__(self, object: str, id: str, name: str, avatar_url: str) -> None:
        self.object = object
        self.id = id
        self.name = name
        self.avatar_url = avatar_url