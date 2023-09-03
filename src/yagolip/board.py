import copy
from random import randint
from typing import Self

from cell import Cell, State


class CellPositionError(Exception):
    def __init__(self: Self, x: int, y: int) -> None:
        super().__init__(
            f"The cell located at ({x},{y}) is in an unhandled position. "
            "We cannot count its neighbours",
        )


def count_alive_cells(*args: Cell) -> int:
    result = 0
    for arg in args:
        result += 1 if arg.get_state() == State.ALIVE else 0
    return result


class Board:
    def __init__(self: Self, cells: list[list[Cell]]) -> None:
        self.width = len(cells)
        self.height = len(cells[0])
        self.cells = cells

    def __str__(self: Self) -> str:
        result = ""
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y].get_state().value:
                    result += " * "
                else:
                    result += "   "
            result += "\n"
        return result

    def _count_neighbours(self: Self, x: int, y: int, reference: list[list[Cell]]) -> int:
        if x == 0 and y == 0:
            neighbours = count_alive_cells(
                reference[x][y + 1],
                reference[x + 1][y],
                reference[x + 1][y + 1],
            )
        elif x == 0 and 0 < y < (self.height - 1):
            neighbours = count_alive_cells(
                reference[x][y - 1],
                reference[x][y + 1],
                reference[x + 1][y - 1],
                reference[x + 1][y],
                reference[x + 1][y + 1],
            )
        elif x == 0 and y == (self.height - 1):
            neighbours = count_alive_cells(
                reference[x][y - 1],
                reference[x + 1][y - 1],
                reference[x + 1][y],
            )
        elif 0 < x < (self.width - 1) and y == 0:
            neighbours = count_alive_cells(
                reference[x - 1][y],
                reference[x - 1][y + 1],
                reference[x][y + 1],
                reference[x + 1][y],
                reference[x + 1][y + 1],
            )
        elif 0 < x < (self.width - 1) and 0 < y < (self.height - 1):
            neighbours = count_alive_cells(
                reference[x - 1][y - 1],
                reference[x - 1][y],
                reference[x - 1][y + 1],
                reference[x][y - 1],
                reference[x][y + 1],
                reference[x + 1][y - 1],
                reference[x + 1][y],
                reference[x + 1][y + 1],
            )
        elif 0 < x < (self.width - 1) and y == (self.height - 1):
            neighbours = count_alive_cells(
                reference[x - 1][y - 1],
                reference[x - 1][y],
                reference[x][y - 1],
                reference[x + 1][y - 1],
                reference[x + 1][y],
            )
        elif x == (self.width - 1) and y == 0:
            neighbours = count_alive_cells(
                reference[x - 1][y],
                reference[x - 1][y + 1],
                reference[x][y + 1],
            )
        elif x == (self.width - 1) and 0 < y < (self.height - 1):
            neighbours = count_alive_cells(
                reference[x - 1][y - 1],
                reference[x - 1][y],
                reference[x - 1][y + 1],
                reference[x][y - 1],
                reference[x][y + 1],
            )
        elif x == (self.width - 1) and y == (self.height - 1):
            neighbours = count_alive_cells(
                reference[x - 1][y - 1],
                reference[x - 1][y],
                reference[x][y - 1],
            )
        else:
            raise CellPositionError(x, y)
        return neighbours

    @classmethod
    def random(cls: type[Self], width: int, height: int) -> Self:
        cells: list[list[Cell]] = []
        for x in range(width):
            cells.append([])
            for _ in range(height):
                cells[x].append(Cell(State.ALIVE) if randint(0, 1) else Cell(State.DEAD))
        return cls(cells)

    def spread_life(self: Self) -> None:
        reference = copy.deepcopy(self.cells)  # Saving the state fo the board before modifying it
        for x in range(self.width):
            for y in range(self.height):
                neighbours = self._count_neighbours(x, y, reference)
                if self.cells[x][y].get_state() == State.ALIVE and neighbours not in (2, 3):
                    self.cells[x][y].set_state(State.DEAD)
                elif (
                    self.cells[x][y].get_state() == State.DEAD
                    and neighbours == 3  # noqa: PLR2004 This value is defined by the rules
                ):
                    self.cells[x][y].set_state(State.ALIVE)
                else:
                    pass  # there are no changes to the cell
