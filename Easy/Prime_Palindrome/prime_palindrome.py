def palindrome(x):
	x = str(x)
	if (x == x[::-1]):
		return True
	else:
		return False

limit = 1000
numbers = list(range(0,limit+1))
numbers[0] = -1
numbers[1] = -1
prime = [2]
running = True

while (running):
	finder = prime[-1] * 2
	while (finder <= limit):
		numbers[finder] = -1
		finder += prime[-1]
	running = False
	for x in numbers:
		if (x != -1 and x > prime[-1]):
			running = True
			prime.append(x)
			break

for x in reversed(prime):
	if (palindrome(x)):
		print(x)
		break
