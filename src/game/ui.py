from src.game import create
from src.systems.debug.fps_label import FpsLabel
from src.systems.graphics.tk_window import TkWindow

display = create(
    TkWindow("Dying space", 640, 480),
    *(() if not __debug__ else (
        FpsLabel(),
    ))
)