from math import degrees
from tkinter import Tk, Canvas, BOTH

from PIL import ImageTk

from src.ecs.tools import flag
from src.tools.vector import Vector


class TkWindow:
    def __init__(self, title, size, camera):
        self.window_root = Tk()
        self.window_root.title(title)
        self.window_root.geometry(f'{size.x}x{size.y}')

        self.title = title
        self.size = size
        self.canvas = Canvas(self.window_root, background='black')
        self.canvas.pack(fill=BOTH, expand=1)

        self.camera = camera

    def __repr__(self):
        return "{{TkWindow: '{0}', size={1}}}".format(self.title, self.size)

    def put(self, entity):
        position = entity.position

        if hasattr(entity, "depth"):
            position = (position * self.camera.depth + (self.camera.position + self.size / 2) * entity.depth) \
                       / (self.camera.depth + entity.depth)

        if not flag(entity, "is_ui"):
            position -= self.camera.position

        for attr, func in {
            "sprite": self.create_image,
            "radius": self.create_circle,
            "is_rectangle": self.create_rectangle,
            "arrow_type": self.create_line,
            "text": self.create_text,
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
            fill=entity.color,
        )

    def create_rectangle(self, position, entity):
        end = position + entity.size
        self.canvas.create_rectangle(
            position.x,
            position.y,
            end.x,
            end.y,
            outline=entity.color
        )

    def create_line(self, position, entity):
        end = position + entity.size
        self.canvas.create_line(
            position.x,
            position.y,
            end.x, end.y,
            fill=entity.color,
            arrow=entity.arrow_type,
        )

    def create_text(self, position, entity):
        self.canvas.create_text(
            position.x, position.y,
            text=entity.text,
            fill=entity.color,
            anchor=entity.anchor,
            font=entity.font,
        )

    def bind_action(self, key, action):
        self.canvas.bind(key, action)

    def get_mouse_position(self):
        return Vector(
            self.window_root.winfo_pointerx() - self.window_root.winfo_rootx(),
            self.window_root.winfo_pointery()- self.window_root.winfo_rooty()
        ) + self.camera.position
