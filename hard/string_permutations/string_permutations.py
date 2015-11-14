import sys
from itertools import permutations

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    all_perms = []
    for perm in permutations(line):
        all_perms.append(''.join(perm))
    print(','.join(sorted(all_perms)))
