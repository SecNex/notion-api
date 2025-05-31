import requests

from ...components.page import Pages, Page
from ...components.blocks import Blocks, Block
from .endpoints import NOTION_SEARCH, NOTION_PAGE, NOTION_BLOCK_CHILDREN

class Client:
    def __init__(self, token: str) -> None:
        self.token = token

    def request(self, url: str, method: str, data: dict = None) -> dict:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }
        response = requests.request(method, url, headers=headers, json=data)
        return response.json()
    
    def search(self, query: str, filter: dict = None) -> Pages:
        url = NOTION_SEARCH
        data = {
            "query": query,
        }
        if filter:
            data["filter"] = filter
        response = self.request(url, "POST", data)
        pages = [Page(**page) for page in response.get('results', [])]
        return Pages(pages=pages)

    def search_pages(self, query: str) -> Pages:
        return self.search(query, filter={
            "property": "object",
            "value": "page"
        })
    
    def search_databases(self, query: str) -> Pages:
        return self.search(query, filter={
            "property": "object",
            "value": "database"
        })
    
    def get_blocks(self, page: Page) -> Blocks:
        url = NOTION_BLOCK_CHILDREN.format(block_id=page.id)
        response = self.request(url, "GET")
        blocks = [Block(**block) for block in response.get('results', [])]
        return Blocks(blocks=blocks)