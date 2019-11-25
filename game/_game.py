from typing import Tuple, Sequence, List, Optional
import random


class Game:
    __val: Sequence
    grid: List[List[int]]

    def __init__(self):
        self.__val = (1, 2, 3)
        self.grid = [[random.choice(self.__val) for i in range(5)] for j in range(5)]

    def turn(self, x1: int, y1: int, x2: int, y2: int):
        temp_x = []
        temp_x[0][0] = self.grid[x1][y1]
        self.grid[x1][y1] = self.grid[x2][y2]
        self.grid[x2][y2] = temp_x[0][0]


