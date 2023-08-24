import numpy as np
import math
class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        return 10 + sum([(alelo **2 - 10 * np.cos(2 * math.pi * alelo)) for alelo in cromosoma])