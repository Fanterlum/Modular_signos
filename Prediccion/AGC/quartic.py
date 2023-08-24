class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        i = 1
        for alelo in cromosoma:
            z +=(i * ( alelo**4 ))
            i+=1
        return z