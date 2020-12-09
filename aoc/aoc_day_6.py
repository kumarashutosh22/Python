from itertools import zip_longest, groupby

lst = open('day6.txt').read().splitlines()

i = (list(g) for _, g in groupby(lst, key=''.__ne__))
lst2 = [a + b for a, b in zip_longest(i, i, fillvalue=[])]

count = 0
for i in lst2:
  count+=len(set(''.join(i)))

print(count)

count2 = 0
for i in lst2:
  count1 = 0
  for j in i:
    if len(j) != 0:
      count1+=1
  for word in set(''.join(i)):
    if ''.join(i).count(word)==count1:
      count2+=1

print(count2)