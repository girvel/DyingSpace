class CircleSprite:
    def __init__(self, radius, color='white', visible=True):
        self.color = color
        self.radius = radius
        self.visible = visible
        self.sprite_type = "circle"
        self.display_radius = radius

    def __repr__(self):
        return "{{CircleSprite: r={0}{1}}}".format(
            self.radius,
            "" if self.visible else ", invisible"
        )
