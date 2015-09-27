import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
    wines, key = line.split(' | ')
    key = set(key)
    wines = wines.split(' ')

    answer = []
    for wine in wines:
        if (key.issubset(set(wine))):
            answer.append(wine)
    if answer:
        print(' '.join(answer))
    else:
        print('False')
