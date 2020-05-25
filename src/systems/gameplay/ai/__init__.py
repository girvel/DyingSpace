from src.ecs.requirements.has import has


def shoot_them_all(ai, enemy):
    if ai is enemy or enemy.radius <= 10:
        return

    delta = enemy.position - ai.position

    if delta and delta.squared_magnitude() <= ai.aggressive_range ** 2:
        ai.rotation = delta.angle()
        ai.shooting_enabled = True


ai = (
    ("ai" | has("flag_ai")) * ("enemy" | has("position", "solid")) >> shoot_them_all,
)
