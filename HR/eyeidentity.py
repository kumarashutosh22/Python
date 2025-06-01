import numpy as np

# for the output to match with hackerrank
np.set_printoptions(legacy='1.13')

print(
  np.eye(              # to get the identity / eye matrix
    *map(              # the * is for unpacking the values
      int,             # mapping the items to integer
      input().split()  # splitting the input on whitespace
    )
  )
)
