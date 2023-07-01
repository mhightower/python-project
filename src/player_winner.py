from src.player import Player

class Winner(Player):
    def __init__(self, player: Player) -> None:
        self.id = player.id
        self.name = player.name
    