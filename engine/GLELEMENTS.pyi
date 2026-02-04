from typing import Tuple, Callable, Optional, Any
from engine.GLANIM import ButtonAnimProfile, ButtonAnimState

# --------- TEXTURE ---------

def load_texture(path: str) -> tuple[int, int, int]: ...
# returns: (texture_id, width, height)


# --------- BUTTON ---------

class GLButton:
    x: float
    y: float
    w: float
    h: float
    color: Tuple[float, float, float]
    on_click: Callable[[], None]

    text: str
    text_color: Tuple[float, float, float]
    text_scale: float

    anim_profile: ButtonAnimProfile

    texture: Optional[int]
    tex_w: int
    tex_h: int

    def __init__(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        color: Tuple[float, float, float],
        on_click: Callable[[], None],
        text: str = "",
        text_color: Tuple[float, float, float] = (1, 1, 1),
        text_scale: float = 6,
        anim_profile: Optional[ButtonAnimProfile] = None,
        texture_path: Optional[str] = None
    ) -> None: ...

    def handle_click(self, window: Any, anim_state: ButtonAnimState) -> None: ...
    def draw(self, anim_state: ButtonAnimState) -> None: ...


# --------- LABEL ---------

class GLLabel:
    x: float
    y: float
    text: str
    color: Tuple[float, float, float]
    scale: float
    max_width: Optional[float]

    def __init__(
        self,
        x: float,
        y: float,
        text: str,
        color: Tuple[float, float, float] = (1, 1, 1),
        scale: float = 10,
        max_width: Optional[float] = None
    ) -> None: ...

    def set_text(self, text: str) -> None: ...
    def draw(self) -> None: ...


# --------- TRANSFORM ---------

class Transform:
    position: list[float]
    rotation: float
    scale: list[float]

    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        rotation: float = 0,
        sx: float = 1,
        sy: float = 1,
        sz: float = 1
    ) -> None: ...

    def translate(self, dx: float, dy: float, dz: float = 0) -> None: ...
    def rotate(self, d: float) -> None: ...
    def set_position(self, x: float, y: float, z: float = 0) -> None: ...
    def set_rotation(self, angle: float) -> None: ...


# --------- BASE OBJECT ---------

class GLObject:
    transform: Transform
    color: Tuple[float, float, float]
    visible: bool

    def draw(self) -> None: ...


# --------- SHAPES ---------

class GLQuad(GLObject):
    width: float
    height: float

    def __init__(
        self,
        width: float,
        height: float,
        color: Tuple[float, float, float] = (1, 1, 1)
    ) -> None: ...

    def draw(self) -> None: ...


class GLCircle(GLObject):
    radius: float
    segments: int

    def __init__(
        self,
        radius: float,
        segments: int = 32,
        color: Tuple[float, float, float] = (1, 1, 1)
    ) -> None: ...

    def draw(self) -> None: ...


class GLCylinder(GLObject):
    radius: float
    height: float
    segments: int

    def __init__(
        self,
        radius: float,
        height: float,
        segments: int = 32,
        color: Tuple[float, float, float] = (1, 1, 1)
    ) -> None: ...

    def draw(self) -> None: ...
