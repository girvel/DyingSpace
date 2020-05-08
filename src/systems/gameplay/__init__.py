from src.systems.gameplay.cleaning import cleaning
from src.systems.gameplay.shooting import shooting

gameplay = (
    *shooting,
    *cleaning,
)
