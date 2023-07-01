import random
from src.rollable import Rollable


class six_sided_die(Rollable):
    def roll(self) -> int:
        return random.randint(1, 6)
