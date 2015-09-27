import sys
import string

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

for line in lines:
    line = line.split(' ')
    line = [ ''.join([word[0].upper(), word[1:]]) for word in line ]
    print(' '.join(line))

