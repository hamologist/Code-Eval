import sys
import string

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()

trans = str.maketrans(string.ascii_letters, string.ascii_uppercase + string.ascii_lowercase)

for line in lines:
    print(line.translate(trans))
