from src.systems.physics.collision import collision
from src.systems.physics.gravity import gravity
from src.systems.physics.inertion import inertia
from src.systems.physics.mounting import mounting
from src.systems.physics.traction import traction

physics = (
    *gravity,
    *traction,
    *collision,
    *inertia,
    *mounting,
)
