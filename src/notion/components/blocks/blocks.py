from ..user import User
from . import Heading, Paragraph
from .component import BlockComponent
from .parent import Parent
from typing import Iterator

class Block:
    def __init__(
            self, 
            object: str,
            type: str,
            id: str, 
            parent: dict, 
            created_time: str, 
            last_edited_time: str,
            last_edited_by: User, 
            created_by: User,
            has_children: bool, 
            archived: bool, 
            in_trash: bool,
            **kwargs
        ) -> None:
        self.object = object
        self.type = type
        self.id = id
        self.parent = Parent(**parent)
        self.created_time = created_time
        self.last_edited_time = last_edited_time
        self.last_edited_by = last_edited_by
        self.created_by = created_by
        self.has_children = has_children
        self.archived = archived
        self.in_trash = in_trash
        self.kwargs = kwargs
        self.component = self.__get_component()

    def __get_component(self) -> BlockComponent:
        if self.type.startswith("heading"):
            return Heading(type=self.type, **self.kwargs[self.type])
        elif self.type == "paragraph":
            return Paragraph(rich_text=self.kwargs[self.type]["rich_text"])
        else:
            return None

class Blocks:
    def __init__(self, blocks: list[Block]) -> None:
        self.blocks = blocks

    def __getitem__(self, index: int) -> Block:
        return self.blocks[index]
    
    def __len__(self) -> int:
        return len(self.blocks)
    
    def __iter__(self) -> Iterator[Block]:
        return iter(self.blocks)