from src.ecs.clocks import delta_time
from src.ecs.requirements import has

movable = "movable" | has("velocity") & has("position")


def apply_velocity(movable):
    movable.position += movable.velocity * delta_time()


inertia = (
    movable >> apply_velocity,
)