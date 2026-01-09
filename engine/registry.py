class Registry:
    items = {}

    @classmethod
    def register_item(cls, item_key: str, item_data: dict):
        cls.items[item_key] = item_data

    @classmethod
    def get_item(cls, item_key: str):
        return cls.items.get(item_key)

    @classmethod
    def has_item(cls, item_key: str) -> bool:
        return item_key in cls.items

