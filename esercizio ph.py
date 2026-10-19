"""
scrivere un programma che data una lista di venti valoridi
ph generati casualmente crei un dizionario cheabbia comechiave
acida, basica, neutrale e come valore il numero di occorrenze
"""
import random
ph={"acida":0,"basica":0,"neutrale":0}
conta_ph=[]
for i in range (0,20):
    conta_ph.append(random.randint(0,14))
for i in conta_ph:
    print(i)
    if i<7:
        print("acida")
    elif i>7:
        print("basica")
    else:
        print("neutrale")
ph["acida"]=i<7
ph["basica"]=i>7
ph["neutrale"]=i==7


