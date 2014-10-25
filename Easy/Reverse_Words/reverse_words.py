import sys

f = open(sys.argv[1])
for x in f.read().split('\n')[0:-1]:
	x = x.rstrip()
	if (x != ""):
		x = x.split(' ')[::-1]
		print(' '.join(x))
