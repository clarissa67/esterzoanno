import random
#procedura
def numeromaggiore(uno,due):
    if uno>due:
        print(uno)
    else:
        print(due)
        
        
        
        
#funzione
def numeromaggioreFunzione(uno,due):
    if uno>due:
        return(uno)
    else:
        return(due)
               
        
if __name__=="__main__":
    numerouno=random.randint(10,30)
    numerodue=random.randint(10,30)
    numeromaggiore(numerouno,numerodue)
    
    maggiore = numeromaggioreFunzione(numerouno,numerodue)
    print(maggiore)  