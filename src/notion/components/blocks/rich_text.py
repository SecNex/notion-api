class Annotations:
    def __init__(self, bold: bool = False, italic: bool = False, strikethrough: bool = False, underline: bool = False, code: bool = False, color: str = "default") -> None:
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color

class Text:
    def __init__(self, content: str, link: dict = None) -> None:
        self.content = content
        self.link = link

class RichText:
    def __init__(self, type: str, text: dict, plain_text: str, annotations: dict = None, href: str = None) -> None:
        self.type = type
        self.text = Text(**text)
        self.plain_text = plain_text
        self.annotations = Annotations(**annotations) if annotations else None
        self.href = href

    def __str__(self) -> str:
        return self.plain_text