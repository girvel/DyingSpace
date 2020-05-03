from math import degrees
from tkinter import Tk, Canvas, BOTH

from PIL import ImageTk

from src.ecs.tools import flag
from src.systems.graphics.sprites.circle_sprite import CircleSprite
from src.systems.graphics.sprites.image_sprite import ImageSprite
from src.systems.graphics.sprites.line_sprite import LineSprite
from src.systems.graphics.sprites.rectangle_sprite import RectangleSprite
from src.systems.graphics.sprites.text_sprite import TextSprite
from src.tools.rectangle import Rectangle
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
        self.display_rectangle = Rectangle(self.camera.position, self.size)
        self.types_dict = {
            "image": self.create_image,
            "circle": self.create_circle,
            "rectangle": self.create_rectangle,
            "line": self.create_line,
            "text": self.create_text,
        }

    def __repr__(self):
        return "{{TkWindow: '{0}', size={1}}}".format(self.title, self.size)

    def put(self, entity):
        position = entity.position

        if hasattr(entity, "depth"):
            position = (position * self.camera.depth + (self.camera.position + self.size / 2) * entity.depth) \
                       / (self.camera.depth + entity.depth)

        if not flag(entity, "is_ui"):
            position -= self.camera.position

        # if not self.display_rectangle.contains(position, entity.display_radius):
        #     return

        self.types_dict[entity.sprite_type](position, entity)

    def create_image(self, position, entity):
        entity.tkinter_sprite = ImageTk.PhotoImage(
            entity.sprite.rotate(-degrees(entity.rotation), expand=True)
            if hasattr(entity, "rotation")
            else entity.sprite
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
        self.window_root.bind(key, action)

    def get_mouse_position(self):
        return Vector(
            self.window_root.winfo_pointerx() - self.window_root.winfo_rootx(),
            self.window_root.winfo_pointery()- self.window_root.winfo_rooty()
        ) + self.camera.position
