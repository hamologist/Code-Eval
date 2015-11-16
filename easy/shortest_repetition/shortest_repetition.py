import sys

def is_repeatable(sub, original):
    if not (len(original) % len(sub)) and sub * int(len(original) / len(sub)) == original:
        return True
    return False

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    match = ''
    shortest = len(line)
    for char in line[0:int(shortest/2)]:
        match += char
        if is_repeatable(match, line):
            shortest = len(match)
            break
    print(shortest)
