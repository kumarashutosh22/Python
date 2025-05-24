# Output the symmetric difference integers in ascending order, one per line.


# a = set(map(int, input().split(' ')))
# b = set(map(int, input().split(' ')))
a = set(map(int, '2 4 5 9'.split(' ')))
b = set(map(int, '2 4 11 12'.split()))

# print(*sorted(a.difference(b).union(b.difference(a))), sep='\n')
print(*sorted(a.symmetric_difference(b)), sep='\n')