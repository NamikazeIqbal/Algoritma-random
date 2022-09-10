from itertools import product,combinations

def func(x, y):
    """
    Showing all possible total function for given domain,and codomain.
    
    x: domain as list
    y: codomain as list
    """
    
    cart_prod = product(x,y)
    com = combinations(cart_prod, len(x))

    sol = []
    
    for i in com:
        lidx = []
        
        for j in i:
            idx = j[0]
            
            if idx in lidx:
                con = True
                break
            else:
                con = False
            
            lidx.append(idx)
        
        if con==False:
            sol.append(i)
        
    
    return sol
