import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums, target_sum = line.split(';')
    nums = [ int(num) for num in nums.split(',') ]
    target_sum = int(target_sum)
    pairs = []

    for y in range(len(nums)):
        for x in range(y+1, len(nums)):
            if nums[y] + nums[x] == target_sum:
                pairs.append('{0},{1}'.format(nums[y], nums[x]))

    if pairs:
        print(';'.join(pairs))
    else:
        print('NULL')
