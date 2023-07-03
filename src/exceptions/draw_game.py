class Draw(Exception):
    '''A game can end in a draw'''
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
