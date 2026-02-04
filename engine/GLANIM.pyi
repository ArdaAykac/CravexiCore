class ButtonAnimProfile:
    hover_brightness: float
    press_scale: float
    press_time: float

    def __init__(
        self,
        hover_brightness: float = ...,
        press_scale: float = ...,
        press_time: float = ...
    ) -> None: ...


class ButtonAnimState:
    hover: bool
    pressed: bool
    scale: float
    color_mul: float


class GLButtonAnimator:
    def __init__(self) -> None: ...
    def update(self, button: object, window: object) -> ButtonAnimState: ...
