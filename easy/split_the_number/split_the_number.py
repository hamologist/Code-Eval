import sys
import re

def create_letter_map(nums, letter_collection):
    letter_map = {}
    for letters in letter_collection:
        for letter in letters:
            if letter not in letter_map:
                letter_map[letter] = nums.pop(0)
    return letter_map
        
f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    line = line.split(' ')
    nums = list(line[0])
    letters = re.findall(r"[\w]+", line[1])
    letter_map = create_letter_map(nums, letters)

    left = int(''.join([letter_map[letter] for letter in letters[0]]))
    right = int(''.join([letter_map[letter] for letter in letters[1]]))

    if '+' in line[1]:
        print(left + right)
    elif '-' in line[1]:
        print(left - right)
