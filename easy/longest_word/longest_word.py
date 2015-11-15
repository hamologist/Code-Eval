import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    line = line.split(' ')   
    longest = 0
    max_word_length = 0
    for x in range(len(line)):
        if len(line[x]) > max_word_length:
            longest = x
            max_word_length = len(line[x])

    print(line[longest])
