import knapsack
import AG

def main():
    pesos = [22, 14, 16, 23, 12, 15, 22, 6, 19, 20, 40, 8, 16, 6, 15, 21, 16]
    valores = [55, 34, 28, 30, 80, 3, 28, 24, 21, 43, 54, 12, 21, 11, 6, 21, 28]
    mochila = knapsack.Knapsack(pesos, valores, 150)
    ag = AG.AG(18, 17, 1, 1200, 0.01, mochila)
    ag.run()

if __name__ == '__main__':
    main()
