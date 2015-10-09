import sys
f = open(sys.argv[1])
lines = f.read().strip().splitlines()

def convert_to_sec(time):
    time = [ int(x) for x in time.split(':') ]
    secs = time[2]
    secs += time[1] * 60
    secs += time[0] * 3600
    return secs

for line in lines:
    line = line.split(' ')
    times = {}
    for time in line:
        times[time] = convert_to_sec(time)
    print(' '.join(sorted(times, key=times.get, reverse=True)))
