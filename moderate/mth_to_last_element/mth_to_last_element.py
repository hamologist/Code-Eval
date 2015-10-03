import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
    vals = line.split(' ')
    index = int(vals.pop())
    if (len(vals) >= index):
        print(vals[-1 * index])
