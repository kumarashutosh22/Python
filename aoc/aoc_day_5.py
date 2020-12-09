lst = open('day5.txt').read().splitlines()

# rows = list(range(127))
# cols = list(range(7))

def rdcdr(ele,rows=list(range(128))):
  if len(ele)==0:
    return rows[0]

  else:
    if ele[0]=='F':
      
      rows = rows[:int(len(rows)/2)]
      
      return rdcdr(ele[1:],rows)
    
    else:
      
      rows = rows[int(len(rows)/2):]
      
      return rdcdr(ele[1:],rows)

def cdcdr(ele,cols=list(range(8))):
  
  if len(ele)==0:
    return cols[0]
    
  else:
    if ele[0]=='L':
      
      cols = cols[:int(len(cols)/2)]
      
      return cdcdr(ele[1:],cols)
    else:
      
      cols = cols[int(len(cols)/2):]
      
      return cdcdr(ele[1:],cols)

seatid = []

for i in lst:
  
    seatid.append(8*rdcdr(i[:-3]) + cdcdr(i[-3:]))

print(max(seatid))

for id in range(min(seatid),max(seatid)+1):
    if id not in seatid:
        print(id)