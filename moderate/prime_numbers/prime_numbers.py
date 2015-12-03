import sys


def primes(num):
    nums = [ x for x in range(2, num) ]
    pos = 0
    while pos < len(nums):
        start = nums[pos]
        x = start * 2
        while x < num:
            if x in nums:
                nums.remove(x)
            x += start
        pos += 1
    return nums


def main():
    f = open(sys.argv[1])
    lines = f.read().strip().splitlines()
    for line in lines:
        print(','.join(str(num) for num in primes(int(line))))


if __name__ == '__main__':
    main()
