class Knapsack:
    def __init__(self, pesos, valores, capacidad):
        self._pesos = pesos
        self._valores = valores
        self._capacidad = capacidad

    def f(self, cromosoma):
        f = 0
        peso = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f = f + self._valores[i]
                peso = peso + self._pesos[i]
        if peso < self._capacidad:
            return f
        else:
            return 0
