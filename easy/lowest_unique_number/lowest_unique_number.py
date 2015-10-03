import sys
from collections import Counter

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

for line in lines:
    nums = [ int(x) for x in line.split(' ') ]
    uniques = [ key for key,value in Counter(nums).items() if value is 1 ]
    if uniques:
        unique = min(uniques)
        print(nums.index(unique)+1)
    else:
        print(0)
