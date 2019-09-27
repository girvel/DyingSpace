from src.ecs.special_entities.named import name_of


class PlayerUi:
    def __init__(self, player):
        self.player = player

    def __repr__(self):
        return f"{{PlayerUi: player={name_of(self.player)}}}"
