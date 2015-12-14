import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums = [ int(num) for num in line.split(' ') ]
    for num in set(nums):
        print(num)

