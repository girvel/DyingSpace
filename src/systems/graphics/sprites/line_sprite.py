from src.tools.vector import Vector


class LineSprite:
    def __init__(self, size=None, color=None, arrow_type=None, visible=True):
        self.size = size if size else Vector.zero
        self.color = color if color else "gray"
        self.arrow_type = arrow_type
        self.visible = visible
        self.sprite_type = "line"
        self.display_radius = abs(self.size)

    def __repr__(self):
        return "{{LineSprite: r={0}{1}}}".format(
            self.size,
            "" if self.visible else ", invisible"
        )
