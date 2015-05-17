import sys
import string

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
	line = ''.join([ x.lower() for x in line ])
	print(line)
