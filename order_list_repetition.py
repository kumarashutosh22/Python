'''
Q. Given a list [1,1,1,2,2,3,4,4,4,4] find give the result in descending order 
from the most frequently repeating element to the least repeating element.
'''
from collections import Counter

lst = [1,1,1,2,2,3,4,4,4,4]

dct = Counter(lst)

print(
    sorted(
        dct,
        key = dct.get,
        reverse = True
        )
    )