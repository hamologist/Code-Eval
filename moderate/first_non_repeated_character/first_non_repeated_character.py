import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    line = list(line)
    while line is not []:
        char = line[0]
        init_len = len(line)
        line = [ x for x in line if x is not char ]
        if len(line) == init_len-1:
            print(char)
            break
