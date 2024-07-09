import numpy as np
from Helpers import constants as const

class Snake:
    def __init__(self) -> None:
        self.bodyPoints = np.zeros(shape=(1, 2), dtype=np.integer)
        self.color = const.BLACK

    def __init__(self, bodyPoints) -> None:
        self.bodyPoints = bodyPoints
        self.color = const.BLACK
