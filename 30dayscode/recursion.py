#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""3""")


def factorial(n):
    if n <= 1:
        return n
    else:
        # Using recursion here
        return n * factorial(n - 1)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + "\n")

    fptr.close()
