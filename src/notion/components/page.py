from .user import User
from .icon import Icon
from .blocks import Blocks, Parent
from .properties import Property, Checkbox, Title, Select, MulitSelect, Number, Email, Url, Date, Verification, UniqueId

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
        if self.icon:
            self.icon = Icon(**self.icon)
        self.parent = Parent(**parent)
        self.archived = archived
        self.in_trash = in_trash
        self.title = properties["Name"]["title"][0]["plain_text"]
        self.properties = self.__get_properties(properties)
        self.url = url
        self.request_id = request_id
        self.public_url = public_url
        self.blocks = blocks
        self.kwargs = kwargs

    def __get_properties(self, properties: dict) -> list[Property]:
        __properties = []
        attributes = properties.keys()
        for attribute in attributes:
            if properties[attribute]["type"] == "checkbox":
                __properties.append(Checkbox(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "email":
                __properties.append(Email(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "title":
                __properties.append(Title(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "select":
                __properties.append(Select(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "multi_select":
                __properties.append(MulitSelect(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "number":
                __properties.append(Number(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "url":
                __properties.append(Url(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "date":
                __properties.append(Date(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "verification":
                __properties.append(Verification(name=attribute, **properties[attribute]))
            elif properties[attribute]["type"] == "unique_id":
                __properties.append(UniqueId(name=attribute, **properties[attribute]))
            else:
                None
        return __properties
    
class Pages:
    def __init__(self, pages: list[Page] = []) -> None:
        self.pages = pages

    def __getitem__(self, index: int) -> Page:
        return self.pages[index]
    
    def __len__(self) -> int:
        return len(self.pages)
    
    def __iter__(self) -> Iterator[Page]:
        return iter(self.pages)