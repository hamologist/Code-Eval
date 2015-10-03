import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

left = '<--<<'
right = '>>-->'

for line in lines:
    count = 0
    for i in range(len(line)-4):
        if line[i:i+5] in (left, right):
            count += 1
    print(count)
