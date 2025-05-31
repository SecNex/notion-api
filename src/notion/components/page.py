from src.notion.components.user import User
from src.notion.components.icon import Icon
from src.notion.components.blocks import Blocks, Block
from src.notion.components.blocks.parent import Parent

from typing import Iterator

class Page:
    def __init__(
            self, 
            object: str,
            id: str,
            created_time: str,
            last_edited_time: str,
            created_by: User,
            last_edited_by: User,
            parent: dict,
            archived: bool,
            in_trash: bool,
            properties: dict,
            url: str,
            cover: str = None,
            icon: Icon = None,
            request_id: str = None,
            public_url: str = None,
            blocks: Blocks = None,
            **kwargs
        ) -> None:
        self.object = object
        self.id = id
        self.created_time = created_time
        self.last_edited_time = last_edited_time
        self.created_by = created_by
        self.last_edited_by = last_edited_by
        self.cover = cover
        self.icon = icon
        self.parent = Parent(**parent)
        self.archived = archived
        self.in_trash = in_trash
        self.properties = properties
        self.url = url
        self.request_id = request_id
        self.public_url = public_url
        self.blocks = blocks
        self.kwargs = kwargs
        self.title = self.properties["Name"]["title"][0]["plain_text"]

class Pages:
    def __init__(self, pages: list[Page] = []) -> None:
        self.pages = pages

    def __getitem__(self, index: int) -> Page:
        return self.pages[index]
    
    def __len__(self) -> int:
        return len(self.pages)
    
    def __iter__(self) -> Iterator[Page]:
        return iter(self.pages)