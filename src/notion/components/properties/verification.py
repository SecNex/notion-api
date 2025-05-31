from .property import Property
from ..user import User

class VerificationProperty:
    def __init__(self, state: str, verified_by: dict, date: str) -> None:
        self.state = state
        self.verified_by = User(**verified_by)
        self.date = date

class Verification(Property):
    def __init__(self, name: str, verification: dict, id: str = None, type: str = "verification") -> None:
        super().__init__()
        self.name = name
        self.verification = VerificationProperty(**verification)
        self.id = id
        self.type = type