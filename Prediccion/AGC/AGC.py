import copy
import numpy as np

class Individuo:
    def __init__(self, alelos, cromosoma):
        self._alelos = alelos
        self._cromosoma = cromosoma
        self._fitness = 0

class AGC:
    def __init__(self, cantidad_individuos, alelos, generaciones, p, problema, maxim = True):
        self._cantidad_individuos = cantidad_individuos
        self._alelos = alelos
        self._generaciones = generaciones
        self._p = p
        self._problema = problema
        self._maxim = maxim
        self._individuos = np.array([])

    def run(self):
        self.crearIndividuos()
        self._mejor_historico = self._individuos[0]
        generacion = 1
        while generacion <= self._generaciones:
            self.evaluaIndividuos()
            self.mejor()
            hijos = np.array([])
            while len(hijos) < len(self._individuos):
                padre1 = self.ruleta()
                padre2 = self.ruleta()
                while padre1 == padre2:
                    padre2 = self.ruleta()
                h1, h2 = self.cruza(self._individuos[padre1], self._individuos[padre2])
                hijos = np.append(hijos, [h1])
                hijos = np.append(hijos, [h2])
            self.mutacion(hijos)
            self._individuos = np.copy(hijos)

            if generacion % 100 == 0:
                print(f'Generación: {generacion} Mejor Histórico: \
{self._mejor_historico._cromosoma} {self._mejor_historico._fitness :.5f}')
            generacion += 1

    def crearIndividuos(self):
        rango = (self._problema.MAX_VALUE - self._problema.MIN_VALUE)
        for i in range(self._cantidad_individuos):
            valores = np.random.random(size = self._alelos)
            cromosoma = self._problema.MIN_VALUE +  valores * rango
            individuo = Individuo(self._alelos, cromosoma)
            self._individuos = np.append(self._individuos, [individuo])

    def evaluaIndividuos(self):
        for i in self._individuos:
            i._fitness = self._problema.fitness(i._cromosoma)
            if not self._maxim:
                i._fitness *= -1

    def ruleta(self):
        f_sum = np.sum([i._fitness for i in self._individuos])
        r = np.random.randint(np.abs(f_sum + 1), dtype = np.int64)
        if f_sum < 0:
            r *= -1
        k = 0
        F = self._individuos[k]._fitness
        if f_sum < 0:
            while F > r and k < len(self._individuos)-1:
                k += 1
                F += self._individuos[k]._fitness
        else:
            while F < r and k < len(self._individuos)-1:
                k += 1
                F += self._individuos[k]._fitness
        return k

    def cruza(self, i1, i2):
        h1 = copy.deepcopy(i1)
        h2 = copy.deepcopy(i2)

        s = self._alelos - 1
        punto_cruza = np.random.randint(s) + 1
        h1._cromosoma[punto_cruza:], h2._cromosoma[punto_cruza:] = h2._cromosoma[punto_cruza:], h1._cromosoma[punto_cruza:]
        return h1, h2

    def mutacion(self, hijos):
        rango = (self._problema.MAX_VALUE - self._problema.MIN_VALUE)
        for h in hijos:
            for a in range(len(h._cromosoma)):
                if np.random.rand() < self._p:
                    h._cromosoma[a] = self._problema.MIN_VALUE + np.random.random() * rango

    def mejor(self):
        for i in self._individuos:
            if i._fitness > self._mejor_historico._fitness:
                self._mejor_historico = copy.deepcopy(i)
