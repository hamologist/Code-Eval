import sys
import math

f = open(sys.argv[1])
lines = f.read().strip().splitlines()
lines = lines[1:]

for line in lines:
    num = int(line)
    max_num = int(math.sqrt(num))
    count = 0
    for x in range(max_num+1):
        value = math.sqrt(num - x**2)
        if value >= x and value == int(value):
            count += 1
    print(count)
