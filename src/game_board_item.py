from abc import ABC, abstractmethod


class GameBoardItem(ABC):
    label = ''

    @abstractmethod
    def get_label(self) -> str:
        pass

    @abstractmethod
    def is_start(self) -> bool:
        pass
