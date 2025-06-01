import numpy as np

n, m = map(int, input().split()) # getting the no. of rows in array

def arr(n):
    return np.array([list(map(int, input().split())) for _ in range(n)]) # converting the list of list to array

a, b = arr(n), arr(n)            # creating the 2 arrays

print(a + b)                     # addition
print(a - b)                     # subtraction
print(a * b)                     # multiplication
print(a // b)                    # division with output as int
print(a % b)                     # modulo
print(a ** b)                    # power
