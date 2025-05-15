class NotionCallout:
    parent_type: str
    type: str
    text: list[str]
    icon: str
    color: str
    
    def __init__(self, parent_type: str, text: list[str], icon: str, color: str) -> None:
        self.parent_type = parent_type
        self.type = "callout"
        self.text = text
        self.icon = icon
        self.color = color
    
    def to_dict(self) -> dict:
        return {
            "object": "block",
            "type": self.type,
            self.type: {
                "rich_text": [{"type": "text", "text": {"content": self.text}}]
            }
        }