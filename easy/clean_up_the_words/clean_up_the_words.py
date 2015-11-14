import sys
import re

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    print(' '.join(re.findall('[a-zA-Z]+', line)).lower())
