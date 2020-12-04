'''
You arrive at the airport only to realize that you grabbed your North Pole 
Credentials instead of your passport. While these documents are extremely 
similar, North Pole Credentials aren't issued by a country and therefore 
aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long 
line has formed for the automatic passport scanners, and the delay could 
upset your travel itinerary.

Due to some questionable network security, you realize you might be able to 
solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble 
detecting which passports have all required fields. The expected fields 
are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each 
passport is represented as a sequence of key:value pairs separated by 
spaces or newlines. Passports are separated by blank lines.
'''

from itertools import zip_longest, groupby

lst = open('day4.txt').read().splitlines()

i = (list(g) for _, g in groupby(lst, key=''.__ne__))
lst2 = [a + b for a, b in zip_longest(i, i, fillvalue=[])]


# 1
# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. In your batch file, how many passports are valid?

'''
The line is moving more quickly now, but you overhear airport security 
talking about how passports with invalid data are getting through. Better 
add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict 
rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both 
present and valid according to the above rules.
'''

# 2
# Count the number of valid passports - those that have all required fields 
# and valid values. Continue to treat cid as optional. In your batch file, 
# how many passports are valid?

valid1 = 0
valid2 = 0

for i in lst2:
  if all(ele in ' '.join(i) for ele in ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
    
    valid1+=1

    ld = {d.split(':')[0]:d.split(':')[1] for d in ' '.join(i).split()}
    
    if (int(ld['byr']) in range(1920,2003)) and (int(ld['iyr']) in range(2010,2021)) and (int(ld['eyr']) in range(2020,2031)):
      
      if (ld['hgt'][-2:] == 'cm' and int(ld['hgt'][:-2]) in range(150,194)) or (ld['hgt'][-2:] == 'in' and int(ld['hgt'][:-2]) in range(59,77)):
        if ld['hcl'][0] == '#' and all(t in 'abcdef0123456789' for t in ld['hcl'][1:]) and len(ld['hcl']) == 7:
          
          if ld['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            
            if ld['pid'].isdigit() and len(ld['pid']) == 9:
              valid2+=1

print(valid1,valid2)