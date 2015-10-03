import sys
import os

size = os.stat(sys.argv[1]).st_size
print(size)
