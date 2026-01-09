from engine.registry import Registry

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_key: str, count=1):
        if not Registry.has_item(item_key):
            print(f"[Inventory] Unknown item: {item_key}")
            return False

        self.items[item_key] = self.items.get(item_key, 0) + count
        return True

    def set_item(self, item_key: str, count: int):
        if not Registry.has_item(item_key):
            print(f"[Inventory] Unknown item: {item_key}")
            return False
    
        if count <= 0:
            self.items.pop(item_key, None)
        else:
            self.items[item_key] = count
    
        return True

