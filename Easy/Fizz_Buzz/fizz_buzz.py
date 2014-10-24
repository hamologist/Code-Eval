import sys

f = open(sys.argv[1])
for x in f.read().split('\n')[0:-1]:
	buzz = []
	x = x.split(' ')
	div1 = int(x[0])
	div2 = int(x[1])
	for y in range(1, int(x[2])+1):
		fizz = ''
		if (y % div1 == 0):
			fizz += 'F'
		if (y % div2 == 0):
			fizz += 'B'
		if (fizz == ''):
			fizz = str(y)
		buzz.append(fizz)
	
	for y in range(0, len(buzz)-1):
		print(buzz[y], end=' ')
	print(buzz[-1])

f.close()
