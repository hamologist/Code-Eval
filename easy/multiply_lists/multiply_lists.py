import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

for line in lines:
    left, right = line.split(' | ')
    left = left.split(' ')
    right = right.split(' ')

    print(' '.join([ str(int(num_left) * int(num_right)) for num_left, num_right in zip(left, right) ]))
