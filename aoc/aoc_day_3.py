'''
With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: 
there's very minimal steering and the area is covered in trees. 
You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. 
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.

These aren't the only trees, though; due to something you read about once involving 
arboreal genetics and biome stability, the same pattern repeats to the right many times.

You start on the open square (.) in the top-left corner and need to reach 
the bottom (below the bottom-most row on your map).
'''
lst = open('day3.txt').read().splitlines()

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# how many trees would you encounter?

right = 3
down = 1
trees = 0

for i in range(0,len(lst),down):
    if (lst[i]*(i+1))[int(right*i/down)] == '#':
        trees += 1

print(trees)

'''
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, 
after all.

Determine the number of trees you would encounter if, for each of the following slopes, 
you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
'''

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

count = 1

for right,down in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
  trees = 0

  for i in range(0,len(lst),down):
    
    if (lst[i]*(i+1))[int(right*i/down)] == '#':
      trees += 1

  count *= trees

print(count)