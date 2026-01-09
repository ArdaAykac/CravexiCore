from engine.registry import Registry

def load_vanilla_item():
    Registry.register_item(
        "game:stone",
        {
         "name": "Stone",
         "item_id": 1,
         "type": "block"
        }
    )
    Registry.register_item(
        "game:wood",
        {
        "name": "Wood",
        "item_id": 2,
        "type": "wood"
        }
    )
