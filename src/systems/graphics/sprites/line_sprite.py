class LineSprite:
    def __init__(self, size, color, arrow_type=None, visible=True):
        self.size = size
        self.color = color
        self.arrow_type = arrow_type
        self.visible = visible

    def __repr__(self):
        return "{{LineSprite: r={0}{1}}}".format(
            self.size,
            "" if self.visible else ", invisible"
        )
