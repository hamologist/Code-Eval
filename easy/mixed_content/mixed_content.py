import sys
f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    words = []
    nums = []
    line = line.split(',')
    for word in line:
        if word.isdigit():
            nums.append(word)
        else:
            words.append(word)
    if (words and nums):
        print(','.join(words) + '|' + ','.join(nums))
    elif words:
        print(','.join(words))
    elif nums:
        print(','.join(nums))
