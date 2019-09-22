class CircleSprite:
    def __init__(self, radius, absolute_displaying=True, visible=True):
        self.visible = visible
        self.absolute_displaying = absolute_displaying
        self.radius = radius

    def display(self, canvas):
        canvas.create_circle(self.position, self.radius, relative=self.absolute_displaying)
