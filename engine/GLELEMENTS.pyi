from OpenGL.GL import *
from _typeshed import Incomplete

class GLButton:
    x: Incomplete
    y: Incomplete
    w: Incomplete
    h: Incomplete
    color: Incomplete
    on_click: Incomplete
    pressed: bool
    def __init__(self, x, y, w, h, color, on_click) -> None: ...
    def update(self, window) -> None: ...
    def draw(self) -> None: ...
