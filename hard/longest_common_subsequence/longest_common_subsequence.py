import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    left,right = line.split(';')
    sequences = []
    right = [x for x in right if x in left ]
    for i in range(len(left)):
        match = False
        if left[i] not in right:
            continue
        for j in range(len(sequences)):
            if right.index(left[i]) > sequences[j][0]:
                match = True
                sequences[j] = (i, sequences[j][1] + list(left[i]))
        if not match:
            sequences.append(( right.index(left[i]), list(left[i]) ))

    largest = []
    for seq in sequences:
        if len(seq[1]) > len(largest):
            largest = seq[1]
    print(''.join(largest))
