"""
for y in range(1, 13):
    print(y, end='')
    for x in range(1, 13):
        print('{0:4d}'.format(x*y), end='')
    print()
"""

for y in range(1, 10):
    print(' ' + str(y), end='')
    for x in range(2, 13):
        print('{0:4d}'.format(x*y), end='')
    print()

for y in range(10, 13):
    print(y, end='')
    for x in range(2, 13):
        print('{0:4d}'.format(x*y), end='')
    print()
