import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    if len(line) <= 55:
        print(line)
    else:
        line = line[:40]
        if ' ' in line:
            line = line[:40-line[::-1].index(' ')-1]
        print("{0}... <Read More>".format(line))
