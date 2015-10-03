import sys

f = open(sys.argv[1])
lines = f.read().split('\n')[:-1]

stack = []

for line in lines:
    numbers = line.split(' ')
    for number in numbers:
        stack.append(number)
    count = 0
    while stack:
        if (count % 2 == 0):
            print(stack.pop(), end=' ')
        else:
            stack.pop()
        count += 1
    print()
