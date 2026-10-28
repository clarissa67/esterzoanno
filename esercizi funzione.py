"""
scrivere un programma che dati due numeri generati casualmente nell'intervallo 10,30
conti e stampi a video il maggiore dei 2 vontrolli è sotto la griglia di 25
"""
import random
def numeromaggioreFunzione (uno,due):
    if uno>due:
        return(uno)
    else:
        return(due)
if __name__=="__main__":
    numerouno=random.randint(10,30)
    numerodue=random.randint(10,30)
    maggiore = numeromaggioreFunzione(numerouno,numerodue)
    print(maggiore)
    if maggiore<25:
        print("sotto soglia")
        #in questo caso i paramentri vengono passati per VALORE (due numeri)
        
    