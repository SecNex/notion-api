from src.notion.components.blocks.parent import BlockComponent
from src.notion.components.blocks.rich_text import RichText

from typing import Any

class Heading(BlockComponent):
    def __init__(self, type: str, rich_text: list[dict], is_toggleable: bool = False, color: str = "default") -> None:
        super().__init__()
        self.type = type
        self.rich_text = [RichText(**text) for text in rich_text]
        self.is_toggleable = is_toggleable
        self.color = color
        self.level = int(type.split("_")[1])