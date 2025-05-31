from .component import BlockComponent
from .rich_text import RichText

class Heading(BlockComponent):
    def __init__(self, type: str, rich_text: list[dict], is_toggleable: bool = False, color: str = "default") -> None:
        super().__init__()
        self.type = type
        self.rich_text = [RichText(**text) for text in rich_text]
        self.is_toggleable = is_toggleable
        self.color = color
        self.level = int(type.split("_")[1])

    def markdown(self) -> str:
        return f"{'#' * self.level} {self.rich_text[0].plain_text}"
    
    def html(self) -> str:
        return f"<h{self.level}>{self.rich_text[0].plain_text}</h{self.level}>"