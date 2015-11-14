import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums, end = line.split(';')
    nums = nums.split(',')
    end = int(end)
    rev_count = int(len(nums)/end)

    for rev in range(0, rev_count):
        pos = rev * end
        nums[pos:pos+end] = nums[pos:pos+end][::-1]
    print(','.join(nums))
