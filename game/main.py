import itertools
from typing import Tuple, Optional


class Field:
    """Класс игрового поля,
    :param size - размер шиина/высота игрового поля
    :param field - список из списков в котором храняться данные о ходах игроков
    """
    def __init__(self, size: int = 3):
        """ Конструктор поля. """
        self.size = size  # prop
        self.__field: list[list[Optional[str]]] = [[None for _ in range(size)] for _ in range(size)]

    def print(self):
        """ Метод вывода на экран игрового поля. """
        for line in self.__field:
            for cell in line:
                if not cell:
                    print("[ ]", end="")
                else:
                    print(f"[{cell}]", end="")
            print()
        print("-" * self.size*3)

    def is_filled(self, line: int, cell: int) -> bool:
        return bool(self.__field[line][cell])

    def fill_cell(self, player_symbol: str, line: int, cell: int) -> bool:
        """ Ход игрока в ячейку поля """
        self.__field[line][cell] = player_symbol
        return self.__check_win(player_symbol, line, cell)

    def __check_win(self, player_symbol: str, line: int, cell: int) -> bool:
        #  горизонтальная проверка
        for cell_ in range(self.size):
            if not self.__field[line][cell_] == player_symbol:
                break
        else:
            return True

        #  вертикальная проверка
        for line_ in range(self.size):
            if not self.__field[line_][cell] == player_symbol:
                break
        else:
            return True

        #  одновременная проверка диагоналей
        for index in range(self.size):
            if not self.__field[index][index] == player_symbol:
                if not self.__field[index][self.size - 1 - index] == player_symbol:
                    return False
        else:
            return True


class Player:
    def __init__(self, number: int, symbol: str):
        self.number = number
        self.symbol = symbol


class TicTacToe:

    @staticmethod
    def __input_cell(field: Field) -> Tuple[int, int]:
        line, cell = [int(part) for part in (input("Введите ячейку: ")).split(" ")]
        while field.is_filled(line, cell):
            line, cell = [int(part) for part in (input("Введите ячейку: ")).split(" ")]
        return line, cell

    def start(self):
        print("Приветствую Вас в игре TicTacToe!")

        player1 = Player(1, 'X')
        player2 = Player(2, '0')

        field = Field(int(input("Введите размер поля: ")))

        for player_ in itertools.cycle([player1, player2]):
            field.print()
            print(f"ходит игрок{player_.number}")

            line, cell = self.__input_cell(field)
            if field.fill_cell(player_.symbol, line, cell):
                field.print()
                print(f"Победил игрок {player_.number}, Поздравляю!")
                return


game = TicTacToe()
game.start()
