from tkinter import W


class TextSprite:
    def __init__(self, text, font, color, anchor=W):
        self.anchor = anchor
        self.color = color
        self.font = font
        self.text = text
