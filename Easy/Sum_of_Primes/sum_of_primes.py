limit = 7925
numbers = list(range(0,limit+1))
prime = [2]
total = 0
running = True

numbers[0] = -1
numbers[1] = -1

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

for x in prime:
	total += x

print(total)
