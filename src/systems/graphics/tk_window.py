from tkinter import Tk, Canvas, BOTH


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

    def bind_action(self, key, action):
        self.__root.bind(key, action)

