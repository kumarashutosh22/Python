import numpy as np

n, m = map(int, input().split())

print(np.prod(np.sum(np.array([list(map(int, input().split())) for _ in range(n)]), axis=0)))
