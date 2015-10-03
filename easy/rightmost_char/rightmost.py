import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()
pos = 0

for line in lines:
    line = line.split(',')
    pos = line[0][::-1].find(line[1])
    if (pos != -1):
        print(len(line[0]) - (pos+1))
    else:
        print(-1)
