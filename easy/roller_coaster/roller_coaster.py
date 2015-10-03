import sys
import string

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
	if (len(line) <= 1000):
		line = list(line)
		cap = True
		for x in range(0, len(line)):
			if (line[x] in string.ascii_letters and cap == True):
				line[x] = line[x].upper()
				cap = False
			elif (line[x] in string.ascii_letters and cap == False):
				line[x] = line[x].lower()
				cap = True
		line = ''.join(line)
		print(line)
