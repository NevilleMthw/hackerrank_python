#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""3""")

if __name__ == "__main__":
    n = int(input().strip())

    for x in range(11):
        result = n * x
        if x > 0:
            print(n, "x", x, "=", result)
