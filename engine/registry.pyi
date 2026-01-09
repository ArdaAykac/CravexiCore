from _typeshed import Incomplete

class Registry:
    items: Incomplete
    @classmethod
    def register_item(cls, item_key: str, item_data: dict): ...
    @classmethod
    def get_item(cls, item_key: str): ...
    @classmethod
    def has_item(cls, item_key: str) -> bool: ...
