import sys

f = open(sys.argv[1])
lines = f.read().rstrip().splitlines()
f.close()
ans = 0

for line in lines:
    ans += int(line)

print(ans)
