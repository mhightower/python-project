from abc import abstractmethod


class Rollable:
    @abstractmethod
    def roll(self) -> int:
        pass
