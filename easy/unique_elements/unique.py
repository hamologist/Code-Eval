import sys

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
    line = [int(x) for x in line.split(',')]
    line = list(set(line))
    print(','.join(map(str, line)))
