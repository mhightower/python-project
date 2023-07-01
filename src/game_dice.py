from src.rollable import Rollable


class game_dice(Rollable):
    def __init__(self, dice01: Rollable, dice02: Rollable) -> None:
        self.dice = [dice01, dice02]

    def roll(self) -> int:
        rtn = sum(map(lambda i: i.roll(), self.dice))
        return rtn
