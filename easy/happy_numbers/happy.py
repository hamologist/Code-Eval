import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()

for line in lines:
    num_list = []
    for x in num:
        num_list.append(int(x)**2)
    new_num = sum(num_list)
    if new_num == 1:
        print(1)
        break
    elif new_num in 
