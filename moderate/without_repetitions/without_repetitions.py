import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    line = list(line)
    pos = 0
    prev = None
    while pos < len(line):
        if prev == line[pos]:
            line.pop(pos)
        else:
            prev = line[pos]
            pos += 1
    print(''.join(line))
