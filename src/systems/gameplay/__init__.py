from src.systems.gameplay.ai import ai
from src.systems.gameplay.cleaning import cleaning
from src.systems.gameplay.shooting import shooting

gameplay = (
    *ai,
    *shooting,
    *cleaning,
)
