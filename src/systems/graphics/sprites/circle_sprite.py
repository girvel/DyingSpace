class CircleSprite:
    def __init__(self, radius, relative_displaying=True):
        self.relative_displaying = relative_displaying
        self.radius = radius

    def display(self, canvas):
        canvas.create_circle(self.position, self.radius, relative=self.relative_displaying)
