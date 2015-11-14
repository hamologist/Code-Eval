import sys


def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    count = 0
    num = line
    while(not is_palindrome(num)):
        num = str(int(num) + int(num[::-1]))
        count += 1
    print("{0} {1}".format(count, num))
