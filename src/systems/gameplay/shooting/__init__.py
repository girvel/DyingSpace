from src.ecs.requirements.has import has
from src.tools.vector import Vector


def shoot(shooter, creator):
    if shooter.shooting_enabled:
        shooter.shooting_enabled = False

        E = shooter.shooting_energy
        m1 = shooter.mass
        m2 = shooter.bullet_prototype.mass

        creator.clocks_creation_list.append(shooter.bullet_prototype.where(
            position=shooter.position + shooter.shooting_offset.rotated(shooter.rotation),
            velocity=shooter.velocity + 2 * E / m2 / (m2 / m1 + 1) * Vector.right.rotated(shooter.rotation),
            rotation=shooter.rotation,
        ))


shooting = (
    ("shooter" | has("shooting_enabled")) * ("creator" | has("clocks_creation_list")) >> shoot,
)
