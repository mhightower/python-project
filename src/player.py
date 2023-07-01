from dataclasses import dataclass

@dataclass
class Player:
    '''Player of the game'''
    id: int
    name: str = 'Player'

    def __hash__(self) -> int:
        return hash(self.id)
    
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Player) and self.id == __value.id