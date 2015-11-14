import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums = [ int(x) for x in line.split(',') ]
    sum = 0
    largest = nums[0]
    for num in nums:
        sum += num
        if largest < sum:
            largest = sum
        if sum < 0:
            sum = 0
    print(largest)
