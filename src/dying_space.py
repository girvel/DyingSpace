from src.ecs.clocks import Clocks
from src.ecs.union import Entity
from src.systems.graphics.graphics import Graphics

clocks = Clocks(
    Graphics()
)

clocks.register_entity(
    Entity(

    )
)
