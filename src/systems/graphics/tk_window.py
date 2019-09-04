from tkinter import Tk, Canvas, BOTH


class TkWindow:
    def __init__(self, title, w, h):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f'{w}x{h}')

        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=1)

    def bind_action(self, key, action):
        self.__root.bind(key, action)
