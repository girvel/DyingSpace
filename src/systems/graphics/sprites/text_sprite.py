from tkinter import W


class TextSprite:
    def __init__(self, text, font, color, anchor=W, visible=True):
        self.visible = visible
        self.anchor = anchor
        self.color = color
        self.font = font
        self.text = text
        self.sprite_type = "text"
        self.display_radius = 10000
