#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
""")

if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # top = sum(arr[0][0:3])
    # mid = arr[1][1]
    # bottom = sum(arr[2][0:3])

    # total = top + mid + bottom

    # print(total)
    total = -64

    for x in range(4):
        for y in range(4):
            total_far = (
                sum(arr[x][y : y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y : y + 3])
            )

            if total < total_far:
                total = total_far

    print(total)
