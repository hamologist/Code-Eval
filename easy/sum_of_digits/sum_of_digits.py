import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
	nums = [ int(x) for x in line ]
	print(sum(nums))
