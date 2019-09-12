from src.systems.physics.collision import collision
from src.systems.physics.gravity import gravity
from src.systems.physics.inertion import inertia
from src.systems.physics.traction import traction

physics = (
    *inertia,
    *gravity,
    *traction,
    *collision,
)
