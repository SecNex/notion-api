from .component import BlockComponent
from .rich_text import RichText

class Paragraph(BlockComponent):
    def __init__(self, rich_text: list[dict] = None) -> None:
        super().__init__()
        self.rich_text = [RichText(**text) for text in rich_text] if rich_text else None
    
    def markdown(self) -> str:
        return "\n".join([text.plain_text for text in self.rich_text])
    
    def html(self) -> str:
        return "<p>" + "\n".join([text.plain_text for text in self.rich_text]) + "</p>"