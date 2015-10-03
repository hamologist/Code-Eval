import sys

f = open(sys.argv[1])
lines = f.read().split('\n')
output = int(lines.pop(0))

lines.sort(key = len)

for x in lines[:output + 1:-1]:
	print(x)

f.close()
