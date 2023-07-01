from abc import ABC, abstractmethod


class GameBoardItem(ABC):
    label = ''

    @abstractmethod
    def get_id(self) -> str:
        pass
