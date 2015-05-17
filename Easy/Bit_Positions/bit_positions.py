import sys
f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]
lines = [ x.split(',') for x in lines ]

for line in lines:
	line = [ int(x) for x in line ]
	if ((line[0] >> (line[1]-1) & 1) == (line[0] >> (line[2]-1) & 1)):
		print('true')
	else:
		print('false')

