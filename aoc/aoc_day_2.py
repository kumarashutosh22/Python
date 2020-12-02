'''
Your flight departs in a few days from the coastal airport;
 the easiest way down to the coast from here is via toboggan.
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers;
 we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted:
some of the passwords wouldn't have been allowed by the
 Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input)
 of passwords (according to the corrupted database) and the corporate policy when that password was set.

Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times 
a given letter must appear for the password to be valid.
'''

# Reading the inputs.
lst = open('day2.txt','r').readlines()


# How many passwords are valid according to their policies?
valid = 0
for i in range(len(lst)):
  lim,plcy,pswrd = lst[i].split()
  l,u = map(int,lim.split('-'))
  wrd = plcy[0]

  if pswrd.count(wrd) in range(l,u+1):
    valid+=1

print(valid)

'''
While it appears you validated the passwords correctly,
 they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy 
rules from his old job at the sled rental place down the street!
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
'''

# How many passwords are valid according to the new interpretation of the policies?
valid = 0
for i in range(len(lst)):
  lim,plcy,pswrd = lst[i].split()
  l,u = map(int,lim.split('-'))
  wrd = plcy[0]

  if (pswrd[l-1] != pswrd[u-1]) & (wrd in pswrd[l-1] + pswrd[u-1]):
    valid+=1

print(valid)