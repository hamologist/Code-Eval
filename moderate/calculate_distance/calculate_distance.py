import sys
import re
import math

f = open(sys.argv[1])
lines = f.read().strip().splitlines()

for line in lines:
    nums = re.findall(r"\((.+), (.+)\) \((.+), (.+)\)", line)[0]
    nums = [ int(num) for num in nums ]
    print(
        int(
            math.sqrt(
                ((nums[0] - nums[2]) ** 2) +
                ((nums[1] - nums[3]) ** 2)
            )
        )
    )
