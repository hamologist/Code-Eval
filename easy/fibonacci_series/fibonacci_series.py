import sys

def calc_fib(n):
	if (n == 0):
		return 0
	if (n == 1):
		return 1
	prev = 0
	answer = 1
	while (n > 1):
		temp = answer
		answer += prev
		prev = temp
		n -= 1
	
	return answer

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
	print(calc_fib(int(line)))

