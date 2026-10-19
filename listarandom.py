#data una lista di 20 elmenti di temperature randomiche dell'intervallo -20, +40
#calcolare il numero di elementi sopra lo 0 e stampare a video la scritta freddo estremo se
#le temperature sotto lo 0 superano quelle sopra, caldo estremo nell altro caso"
import random
listatemperatura=[]
for i in range(0,20):
    listatemperatura.append(random.radiant(-20,40))
    
sopra=0
sotto=0

for temperatura in listatemperatura:
    if temperatura>0:
        sopra=sopra+1
    else:
        sotto=sotto+1

if sopra>sotto:
    print("calso estremo")
elif sotto>sopra:
    print("freddo estremo")
else:
    print("indecisione")
