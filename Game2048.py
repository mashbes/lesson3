import numpy as np
import random


class Game:
    def __init__(self, row=4, col=4):
        self.row = row
        self.col = col
        self.score = 0
        self.field = np.array([[0 for col in range(self.row)] for row in range(self.col)])

    def swap(self, row, col, route):
        tmp_value = self.field[row][col]
        self.field[row + route][col] = tmp_value
        self.field[row][col] = 0

    def move_left(self):
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_right(self):
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_up(self):
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def move_down(self):
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def has_moves(self):
        for row in self.field:
            for cell in row:
                if cell == 0:
                    return  True
        return  False


    def get_score(self):
        return self.score

    def get_field(self):
        if self.has_moves():
            count = 0
            while count < 2:
                row = random.randint(0, 3)
                cell = random.randint(0, 3)
                if self.field[row][cell] == 0:
                     if random.randint(1,10) < 9:
                         self.field[row][cell] = 2
                     else:
                         self.field[row][cell] = 4
                     count += 1
        return self.field

def main():
    game = Game()

    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))

        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))

        if not game.has_moves():
            print("No available moves left, game over.")
            break

        print("W, A, S, D - move")
        print("Q - exit")

        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if c in ('a', 'A'):
            game.move_left()
        elif c in ('d', 'D'):
            game.move_right()
        elif c in ('w', 'W'):
            game.move_up()
        elif c in ('s', 'S'):
            game.move_down()
        elif c in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    main()
