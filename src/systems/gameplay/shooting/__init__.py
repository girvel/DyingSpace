from src.ecs.requirements.has import has
from src.tools.vector import Vector


def shoot(gun, creator):
    if gun.shooting_enabled:
        gun.shooting_enabled = False

        bullet = gun.bullet_constructor()
        dv = gun.shooting_velocity * Vector.right.rotated(gun.rotation)
        creator.clocks_creation_list.append(bullet.set(
            position=gun.position + gun.shooting_offset.rotated(gun.rotation),
            velocity=gun.velocity + dv,
            rotation=gun.rotation,
        ))

        gun.velocity -= bullet.mass * dv / gun.mass


shooting = (
    ("gun" | has("shooting_enabled")) * ("creator" | has("clocks_creation_list")) >> shoot,
)
