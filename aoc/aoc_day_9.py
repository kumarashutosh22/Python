from itertools import combinations

lst = list(map(int,open('day9.txt').read().splitlines()))

rule_breaker=0
for i in range(25,len(lst)):
  if lst[i] not in list(a+b for a,b in combinations(lst[i-25:i],2)):
    rule_breaker = lst[i]

print(rule_breaker)

check = []
solving = True
while solving:

  if sum(check)<rule_breaker:
    check.append(lst.pop(0))

  elif sum(check)>rule_breaker:
    check.pop(0)
  elif sum(check)==rule_breaker:
    print(min(check),'+',max(check),'=',min(check)+max(check))
    solving=False