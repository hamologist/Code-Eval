import sys

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
	count = len(line)
	print(count)

