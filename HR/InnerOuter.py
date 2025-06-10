import numpy as  np # for numerical operations

# input() reads a line from the user (e.g., "1 2 3").
# split() splits it into a list of strings: ['1', '2', '3'].
# map(int, ...) applies the int() function to each string, converting them to integers.
# list(...) converts the map object into a Python list: [1, 2, 3].
# np.array(...) creates a 1D NumPy array (a vector) from the list.

a, b = np.array(list(map(int, input().split()))), np.array(list(map(int, input().split())))

# np.inner(a, b): Computes the inner product of the two vectors.
# For 1D vectors, this is the same as the dot product. It results in a single number (scalar).
# It's calculated as: a[0]*b[0] + a[1]*b[1] + ...

# np.outer(a, b): Computes the outer product of the two vectors.
# This creates a matrix where each element (i, j) is the product of a[i] and b[j].
# If 'a' has M elements and 'b' has N elements, the result is an M x N matrix.

# sep='\n': This argument in the print function ensures that the results of the
# inner and outer products are printed on separate lines.

print(np.inner(a, b), np.outer(a, b), sep='\n')
