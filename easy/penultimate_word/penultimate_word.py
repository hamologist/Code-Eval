import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    print(line.split(' ')[-2])
