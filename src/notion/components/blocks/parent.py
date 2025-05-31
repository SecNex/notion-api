class Parent:
    def __init__(self, type: str, page_id: str = None, database_id: str = None, block_id: str = None, workspace: bool = False) -> None:
        self.type = type
        self.page_id = page_id
        self.database_id = database_id
        self.block_id = block_id
        self.workspace = workspace