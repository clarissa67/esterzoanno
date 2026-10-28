import random
def numeromaggiore(uno,due):
    if uno>due:
        print(uno)
    else:
        print(due)
if __name__=="__main__":
    numerouno=random.randint(10,30)
    numerodue=random.randint(10,30)
    numeromaggiore(numerouno,numerodue)