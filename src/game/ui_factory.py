class UiFactory:
    def __init__(self, ui_position, compass_size):
        self.ui_position = ui_position
        self.compass_size = compass_size

    def produce(self, holder):
        display_center = self.ui_position + self.compass_size / 2

