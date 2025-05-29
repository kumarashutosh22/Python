k, a = int(input()), list(map(int, input().split(" ")))

print((sum(set(a))*k - sum(a))//(k-1))
