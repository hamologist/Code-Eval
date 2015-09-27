import sys
import re
from collections import Counter

regex = re.compile('[^a-zA-Z]')

f = open(sys.argv[1])
for line in f.read().split('\n')[0:-1]:
	beauty = 26
	answer = 0

	line = line.lower()
	line = regex.sub('', line)
	count = Counter(line)

	for key,value in sorted(count.items(), key=lambda x: x[1], reverse=True):
		answer += value * beauty
		beauty -= 1
	
	print(answer)
