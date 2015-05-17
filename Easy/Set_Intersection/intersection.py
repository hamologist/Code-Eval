import sys
f = open(sys.argv[1])
lines = f.read().strip().split('\n')

for line in lines:
    line = line.split(';')
    left = [int(x) for x in line[0].split(',')]
    right = [int(x) for x in line[1].split(',')]
    intersection = list(set(left).intersection(set(right)))
    intersection.sort()
    print(','.join(map(str, intersection)))
