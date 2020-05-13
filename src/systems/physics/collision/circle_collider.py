from src.systems.physics.collision.collider import Collider


class CircleCollider(Collider):
    def __init__(self, radius, resilience_k=0):
        Collider.__init__(self, resilience_k)
        self.radius = radius
