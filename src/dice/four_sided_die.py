from src.rollable import Rollable
import random

class four_sided_die(Rollable):
    def roll(self) -> int:
        random_number = random.randint(1, 4)
        return random_number
