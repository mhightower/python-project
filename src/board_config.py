import csv
from src.game_board import GameBoard


class BoardReader:
    board = []

    def __init__(self, csv_board_file: str):
        with open(csv_board_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.__process_board_config(csvreader)

    def get_board(self) -> GameBoard:
        return GameBoard(self.board)

    def __process_board_config(self, input):
        for sublist in input:
            sublist = sublist[:-1]
            if input.line_num % 2 == 1:
                sublist.reverse()
                self.board = sublist + self.board
            else:
                self.board = sublist + self.board
