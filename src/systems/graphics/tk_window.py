from tkinter import Tk, Canvas, BOTH

from PIL import ImageTk


class TkWindow:
    def __init__(self, title, size, camera_target=None, camera_position=None):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f'{size.x}x{size.y}')

        self.size = size
        self.canvas = Canvas(self.__root, background='black')
        self.canvas.pack(fill=BOTH, expand=1)

        self.camera_target = camera_target
        self.camera_position = camera_position

    def create_image(self, position, sprite, rotation=0, relative=True):
        if relative:
            position -= self.camera_position

        sprite.current_tk_version = ImageTk.PhotoImage(sprite.rotate(rotation, expand=True))
        self.canvas.create_image(
            position.x, position.y,
            image=sprite.current_tk_version,
        )

    def create_circle(self, position, radius, relative=True, fill='white'):
        if relative:
            position -= self.camera_position

        self.canvas.create_oval(
            position.x - radius,
            position.y - radius,
            position.x + radius,
            position.y + radius,
            fill=fill
        )

    def bind_action(self, key, action):
        self.__root.bind(key, action)

