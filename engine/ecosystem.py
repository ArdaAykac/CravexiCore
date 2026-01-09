import os
import json
import mmap
import time


#cls = class demek  self ile aynı şey istediğim şeyi yazabilirim

class New_Game:
    base_folder = "database"
    current_game =None
    game_types = None

    game_types = {
        "game name": 0,
        "networking": 1,
        "Games":2,
    }

    @classmethod
    def new_game(cls, game_name,networking=False,):
        cls.current_game = [game_name,networking]
        game_path = os.path.join(cls.base_folder, game_name)
        os.makedirs(game_path, exist_ok=True)
        



class SaveSystem:
    base_folder = "database"

    @classmethod
    def save_inventory(cls, game_name, inventory, filename="inventory.json"):
        game_path = os.path.join(cls.base_folder, game_name)
        os.makedirs(game_path, exist_ok=True)

        file_path = os.path.join(game_path, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(inventory.items, file, indent=4, ensure_ascii=False)

    @classmethod
    def load_inventory(cls, game_name, inventory, filename="inventory.json"):
        file_path = os.path.join(cls.base_folder, game_name, filename)

        if not os.path.exists(file_path):
            inventory.items = {}
            return

        with open(file_path, "r", encoding="utf-8") as file:
            inventory.items = json.load(file)
            print("Succesfuly")
        
    @classmethod
    def list_games(cls,list_games=False,folders_path="database"):
        if not list_games:
            print(f"<Debug_SVS>{list_games}")
            ValueError
        print(f"<Debug_SVS{os.listdir(folders_path)}")




class debug_system:

    @staticmethod
    def debug(arg, *game_types, debug=False):

        if not debug:
            print("<Debug> is False")
            return

        if not game_types:
            print("<Debug> No game type provided")
            return

        print("Debug is active")

        for game_type in game_types:
            if not isinstance(game_type, str):
                continue

            normalized = game_type.replace("İ", "I").lower()

            for key_game_type, index in New_Game.game_types.items():
                if key_game_type.lower() == normalized:
                    value = New_Game.current_game[index]
                    print(f"<{key_game_type}>: {value}")
                    break
            else:
                print(f"<{game_type}>: There is no such game type")



class RAMManager:
    def __init__(self, size_kb: int):
        self.size = size_kb * 1024
        self.mem = mmap.mmap(-1, self.size)
        self.offset = 0
        self.index = {}

    def store(self, key: str, data: bytes):
        size = len(data)

        if self.offset + size > self.size:
            raise MemoryError("RAM dolu")

        start = self.offset
        self.mem[start:start + size] = data
        self.index[key] = (start, size)
        self.offset += size

    def load(self, key):
        start, size = self.index[key]
        return memoryview(self.mem)[start:start + size]
    



class Behaviour:
    def awake(self):
        pass

    def start(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass




class GameLoop:
    def __init__(self, target_fps=60, debug=False):
        self.objects = []
        self.running = False
        self.started = False
        self.target_fps = target_fps
        self.debug = debug

    def log(self, *args):
        if self.debug:
            print(*args)


    def add(self, obj):
        self.objects.append(obj)
        obj.game = self

        
        if hasattr(obj, "awake"):
            obj.awake()

        self.log(f"[GameLoop] Awake -> {obj.__class__.__name__}")

  

    def run(self):
        self.running = True
        last_time = time.time()

  
        if not self.started:
            for obj in self.objects:
                if hasattr(obj, "start"):
                    obj.start()
            self.started = True

        self.log("[GameLoop] Started")

        while self.running:
            now = time.time()
            dt = now - last_time
            last_time = now

            for obj in self.objects[:]:  
                if hasattr(obj, "update"):
                    obj.update(dt)

            time.sleep(1 / self.target_fps)

        self.log("[GameLoop] Stopped")

    def stop(self):
        self.running = False



