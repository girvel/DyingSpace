from math import degrees
from tkinter import Tk, Canvas, BOTH, W

from PIL import ImageTk

from src.ecs.tools import flag


class TkWindow:
    def __init__(self, title, size, camera_target=None, camera_position=None):
        self.window_root = Tk()
        self.window_root.title(title)
        self.window_root.geometry(f'{size.x}x{size.y}')

        self.title = title
        self.size = size
        self.canvas = Canvas(self.window_root, background='black')
        self.canvas.pack(fill=BOTH, expand=1)

        self.camera_target = camera_target
        self.camera_position = camera_position
        self.camera_depth = 1

    def __repr__(self):
        return "{{TkWindow: '{0}', size={1}}}".format(self.title, self.size)

    def put(self, entity):
        position = entity.position

        if hasattr(entity, "depth"):
            position = (position * self.camera_depth + (self.camera_position + self.size / 2) * entity.depth) \
                       / (self.camera_depth + entity.depth)

        if not flag(entity, "relative_displaying"):
            position -= self.camera_position

        for attr, func in {
            "sprite": self.create_image,
            "radius": self.create_circle,
            "rectangle_begin": self.create_rectangle,
        }.items():
            if hasattr(entity, attr):
                func(position, entity)
                return

    def create_image(self, position, entity):
        entity.tkinter_sprite = ImageTk.PhotoImage(
            entity.sprite.rotate(-degrees(entity.rotation), expand=True)
            if hasattr(entity, "rotation") else entity.sprite
        )

        self.canvas.create_image(
            position.x, position.y,
            image=entity.tkinter_sprite,
        )

    def create_circle(self, position, entity):
        self.canvas.create_oval(
            position.x - entity.radius,
            position.y - entity.radius,
            position.x + entity.radius,
            position.y + entity.radius,
            fill='white',
        )

    def create_rectangle(self, position, entity):
        end = position + entity.size
        self.canvas.create_rectangle(
            position.x,
            position.y,
            end.x,
            end.y,
            outline=entity.border_color
        )

    def create_line(self, position, size, relative=True, fill='white', arrow=None):
        if relative:
            position -= self.camera_position

        end = position + size
        self.canvas.create_line(
            position.x, position.y,
            end.x, end.y,
            fill=fill,
            arrow=arrow,
        )

    def create_text(self, position, text, relative=True, fill='white', anchor=W, font="Consolas 10"):
        if relative:
            position -= self.camera_position

        self.canvas.create_text(
            position.x, position.y,
            text=text,
            fill=fill,
            anchor=anchor,
            font=font
        )

    def bind_action(self, key, action):
        self.window_root.bind(key, action)

