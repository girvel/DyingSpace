class CircleSprite:
    def __init__(self, radius):
        self.radius = radius

    def display(self, canvas, d):
        p = self.position - d
        canvas.create_oval(
            p.x - self.radius,
            p.y - self.radius,
            p.x + self.radius,
            p.y + self.radius,
            fill='white'
        )
