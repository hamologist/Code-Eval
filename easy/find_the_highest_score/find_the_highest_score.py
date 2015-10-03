import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

for line in lines:
    table = [ [ int(cols) for cols in rows.split(' ') ] for rows in line.split(' | ') ]
    for col in list(zip(*table)):
        print(max(col), end=' ')
    print()
