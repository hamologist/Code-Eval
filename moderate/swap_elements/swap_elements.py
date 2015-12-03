import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums, swaps = line.split(' : ')
    nums = [ int(num) for num in nums.split(' ') ]
    swaps = [ [ int(num) for num in swap.split('-') ] for swap in swaps.split(', ') ]
    for swap in swaps:
        temp = nums[swap[0]]
        nums[swap[0]] = nums[swap[1]]
        nums[swap[1]] = temp
    print(' '.join([ str(num) for num in nums ]))
