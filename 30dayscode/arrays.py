#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

# Reverse an array
sys.stdin = StringIO("""1
    1 2 3 4
    """)
if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse()

    print(arr)
