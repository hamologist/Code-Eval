import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    line = [int(num) for num in line.split(' ')]
    length = line[0]
    distance = line[1]
    num_of_bats = line[2]
    bats = line[3:]

    if num_of_bats:
        bats.sort()
        answer = 0

        first = bats[0] - 6
        answer += int(first / distance)

        for x in range(len(bats)-1):
            answer += int((bats[x+1] - bats[x]) / distance) - 1
            
        last = (length - 6) - bats[-1]
        answer += int(last / distance)
    else:
        usable = length - 12
        answer = int(usable / distance) + 1

    print(answer)
        
