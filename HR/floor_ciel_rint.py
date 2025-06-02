import numpy as np
np.set_printoptions(legacy='1.13')

a = np.array(list(map(float, input().split())))

print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')
