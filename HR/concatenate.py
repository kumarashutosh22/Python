import numpy as np

m, n, p = map(int, input().split(' '))

def arr_cr(a):
    
    l = []
    
    for _ in range(a):
        l.append(list(map(int, input().split(' '))))
        
    return np.array(l)
    
print(np.concatenate((arr_cr(m),arr_cr(n)), axis=0))
