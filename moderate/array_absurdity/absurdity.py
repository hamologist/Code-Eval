import sys

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
    line = line.split(';')[1].split(',')
    line = [x for x in line if line.count(x) > 1]
    print(line[0])
