from engine.items import load_vanilla_item
from engine.registry import Registry
from engine.inventory import Inventory
from engine.ecosystem import Behaviour, GameLoop
from engine.GUIS import *
from engine.GLELEMENTS import GLButton
import time



class Game(Behaviour):
    def awake(self):
        self.app = OPD2(600, 600, "OpenGL UI + Ecosystem")

        # 0 = kırmızı, 1 = mavi
        self.state = 0
        self.app.background_color = (1.0, 0.0, 0.0, 1.0)

        def on_click():
            self.state = 1 - self.state

            if self.state == 0:
                self.app.background_color = (1.0, 0.0, 0.0, 1.0)
            else:
                self.app.background_color = (0.2, 0.4, 0.8, 1.0)

        self.button = GLButton(
            x=200,
            y=250,
            w=200,
            h=80,
            color=(1.0, 1.0, 0.0),
            on_click=on_click
        )

    def update(self, dt):
        if self.app.should_close():
            self.game.stop()
            self.app.terminate()
            return

        self.app.begin_frame()

        self.button.update(self.app.window)
        self.button.draw()

        self.app.end_frame()


game_runner = GameLoop(target_fps=60)
game = Game()
game_runner.add(game)
game_runner.run()