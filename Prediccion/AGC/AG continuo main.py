import sphere
import quartic
import rastrigin
import rosenbrock
import AGC
#import random

def main():
    __DIMENSIONES = [2,4,8]
    GENERACIONES = 2000
    INDIVIDUOS = 64
    FP = 0.08
    rDimenciones = 2
    s = sphere.Sphere()
    s_Ag=[]
    q = quartic.Quartic()
    q_Ag=[]
    rA = rastrigin.Rastrigin()
    rA_Ag=[]
    rO = rosenbrock.Rosenbrock()
    rO_Ag=[]

    for dimension in __DIMENSIONES:
        print(f'dimenciones agregadas: {dimension}')
        s_Ag.append(AGC.AGC(INDIVIDUOS, dimension , GENERACIONES, FP, s, False))
        q_Ag.append(AGC.AGC(INDIVIDUOS, dimension , GENERACIONES, FP, q , False))
        rA_Ag.append(AGC.AGC(INDIVIDUOS, dimension , GENERACIONES, FP, rA, False))
        rO_Ag.append(AGC.AGC(INDIVIDUOS, dimension , GENERACIONES, FP, rO, False))
    
    '''while rDimenciones == 1:
        rd = random.randint(0,2)
        print(f'dimenciones agregadas: {rd}')
        s_Ag.append(AGC.AGC(INDIVIDUOS, __DIMENSIONES[rd] , GENERACIONES, FP, s, False))
        q_Ag.append(AGC.AGC(INDIVIDUOS, __DIMENSIONES[rd]  , GENERACIONES, FP, q , False))
        rA_Ag.append(AGC.AGC(INDIVIDUOS, __DIMENSIONES[rd] , GENERACIONES, FP, rA, False))
        rO_Ag.append(AGC.AGC(INDIVIDUOS, __DIMENSIONES[rd] , GENERACIONES, FP, rO, False))
        rDimenciones-=1'''

    print("sphere")
    for i in range(0,len(s_Ag)):
        s_Ag[i].run()

    '''print("quartic")
    for i in range(0,len(q_Ag)):
        q_Ag[i].run()
    print("rastrigin")
    for i in range(0,len(rA_Ag)):
        rA_Ag[i].run()
    print("rosenbrock")
    for i in range(0,len(rO_Ag)):
        rO_Ag[i].run()'''
        
if __name__ == '__main__':
    main()
