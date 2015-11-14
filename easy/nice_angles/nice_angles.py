import sys

f = open(sys.argv[1])
lines = [ float(x) for x in f.read().strip().splitlines() ]

for line in lines:
    decimal = line % 1
    whole_number = str(int(line))
    minutes = str(int(decimal * 60))
    seconds = str(int(decimal * 60 % 1 * 60))

    print("{0}.{1}'{2}\"".format(whole_number, minutes.zfill(2), seconds.zfill(2)))
