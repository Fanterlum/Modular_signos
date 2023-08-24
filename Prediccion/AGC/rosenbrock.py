class Rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for nAlelo in range(len(cromosoma)-1):
            z +=(100.0*(cromosoma[nAlelo+1]-cromosoma[nAlelo]**2)**2 + (cromosoma[nAlelo]-1)**2)
        return z