class CircleSprite:
    def __init__(self, radius):
        self.radius = radius

    def display(self, canvas):
        canvas.create_oval(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.position.x + self.radius,
            self.position.y + self.radius,
            fill='white'
        )
