class ImageSprite:
    def __init__(self, sprite):
        self.sprite = sprite

    def display(self, canvas):
        canvas.create_image(self.position.x, self.position.y, image=self.sprite)
