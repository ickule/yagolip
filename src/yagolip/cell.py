from enum import Enum
from typing import Self


class State(int, Enum):
    ALIVE = 1
    DEAD = 0


class Cell:
    def __init__(self: Self, state: State = State.DEAD) -> None:
        self._state = state

    def get_state(self: Self) -> State:
        return self._state

    def set_state(self: Self, state: State) -> None:
        self._state = state
