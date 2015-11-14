import sys

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    encoded, keys = line.split('|')
    keys = keys.strip().split(' ')
    decode = []
    decode = [ encoded[int(key)-1] for key in keys ]
    print("".join(decode))
