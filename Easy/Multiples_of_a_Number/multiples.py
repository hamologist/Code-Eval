import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

for line in lines:
	line = line.split(',')

	x = int(line[0])
	n = int(line[1])
	mult = 2

	while(x > n * mult):
		mult += 1
	
	print(n * mult)
