import sys
import string

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
    test = set()
    line = line.lower()
    for char in line:
        test |= {char}
    isNull = True
    for char in string.ascii_lowercase:
        if char not in test:
            print(char, end='')
            isNull = False
    if isNull:
        print('NULL', end='')
    print()
