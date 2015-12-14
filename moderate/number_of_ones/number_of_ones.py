import sys
import collections

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    print(collections.Counter(bin(int(line)))['1'])
