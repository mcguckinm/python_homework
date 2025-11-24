#Task 6

from sqlalchemy import false


class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
    pass

class Board:
    valid_moves = ["upper left", "upper middle", "upper right", "middle left", "center", "middle right", "lower left", "lower middle", "lower right"]
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
    def make_move(self, player, row, col):
        if self.board[row][col] != " ":
            raise TictactoeException("Cell is already occupied")
        self.board[row][col] = player

    def __str__(self):
        lines = []
        lines.append(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} \n")
        return "".join(lines)
    
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def what_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): #check columns
            if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i] != " ":
                win = True
                break
        if not win:
            for i in range(3): #check rows
                if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2] != " ":
                    win = True
                    break
        if not win: #check diagonals
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
                win = True
            elif self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
                win = True
        if not win:
            if self.turn == "X":
                return (False, "Player X's turn.")
            else:
                return (False, "Player O's turn.")
        else:
            if self.turn == "X":
                return (True, "Player O wins!")
            else:
                return (True, "Player X wins!")
                