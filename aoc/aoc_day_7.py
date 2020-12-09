lst = open('day7.txt').read().splitlines()

bagorama = {}
for i in lst:
  carrier = i.split(' bag')[0]
  bags = []
  for bag in i.split(' bag')[1:]:
    if len(bag)>2:
      bags.append(' '.join(bag.split()[-2:]))
  
  bagorama[carrier] = bags



shinyin = set()
i = 0

while i < len(bagorama):
  for carrier in bagorama:
    if 'shiny gold' in bagorama[carrier]:
      # adding carrier bags having shiny gold in them
      shinyin.add(carrier)
    for bag in bagorama[carrier]:
      # adding carrier bags having the above added bags in them
      if bag in shinyin:
        shinyin.add(carrier)
  i+=1
      

print(len(shinyin))

def totbag(color):
  return 1 + sum(totbag[inbag] for inbag in bagorama[color])

# totbag['shiny gold']