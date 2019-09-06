from src.systems.physics.collision import collision
from src.systems.physics.gravity import gravity
from src.systems.physics.inertion import inertia

physics = (
    *inertia,
    *gravity,
    *collision,
)
