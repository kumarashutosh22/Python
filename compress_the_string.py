# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
# For a better understanding of the problem, check the explanation.

# Input Format
# A single line of input consisting of the string S.
# Sample input - 1222311

# Output Format
# A single line of output consisting of the modified string.
# Sample output - (1, 1) (3, 2) (1, 3) (2, 1)

from itertools import groupby

# print(' '.join([f"({len(list(g))}, {i})" for i,g in groupby(input())]))
# print(' '.join([f"({len(list(g))}, {i})" for i,g in groupby('1222311')]))
print(' '.join(f"({sum(1 for _ in g)}, {i})" for i, g in groupby('1222311')))