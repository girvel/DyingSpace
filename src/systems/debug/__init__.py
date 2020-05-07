from src.systems.debug.data_display import data_display
from src.systems.debug.fps import fps_monitor

debug = (
    *fps_monitor,
    *data_display,
)
