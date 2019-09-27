class CircleSprite:
    def __init__(self, radius, visible=True):
        self.visible = visible
        self.radius = radius

    def __repr__(self):
        return "{{CircleSprite: r={0}{1}}}".format(
            self.radius,
            "" if self.visible else ", invisible"
        )
