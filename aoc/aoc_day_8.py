lst = open('day8.txt').read().splitlines()

i=0
c = 0
done = []
jump = []
while i not in done:
  done.append(i)
  if 'n' in lst[i]:
    i+=1
  elif 'j' in lst[i]:
    jump.append(i)
    i = eval('i'+lst[i].split()[1])
  elif 'a' in lst[i]:
    c = eval('c'+lst[i].split()[1])
    i+=1

print(c)


for j in jump:
    
  i = 0
  c=0
  done=[]

  lst2 = lst.copy()
  lst2[j] = 'nop' + lst2[j][3:]

  while i not in done and i != len(lst2):
    done.append(i)
    
    if 'n' in lst2[i]:
      i+=1
    
    elif 'j' in lst2[i]:
      i = eval('i'+lst2[i].split()[1])
      
    elif 'a' in lst2[i]:
      c = eval('c'+lst2[i].split()[1])
      i+=1

  if i == len(lst2):
    print(c)