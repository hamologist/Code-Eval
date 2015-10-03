import sys

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

for line in lines:
    is_jolly = True
    line = line.strip().split(' ')
    line = [int(x) for x in line]
    n_val = line[0]
    for x in range(1, len(line)-1):
        if abs(line[x] - line[x+1]) != n_val - (x):
            is_jolly = False
            print('Not jolly')
            break
    if is_jolly:
        print('Jolly')
