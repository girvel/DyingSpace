from tkinter import PhotoImage


class ImageSprite:
    def __init__(self, name=None):
        self.sprite = PhotoImage(file=f'../assets/sprites/{name}.gif') if name else None

    def display(self, canvas):
        canvas.create_image(self.position.x, self.position.y, image=self.sprite)
