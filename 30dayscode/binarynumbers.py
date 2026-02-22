#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""439""")

if __name__ == "__main__":
    n = int(input().strip())

    # We assume the value is an integer and we convert to a binary format
    # Once in binary format we can get the maximum of 1's

    new_n = bin(n)
    # Remove the 0b
    new_n = new_n[2:]
    # Split based on the 0 in base-10 integer
    new_n = new_n.split("0")

    # Create a new list and append the lengths of the 1's
    # and get the maximum
    new_length = []
    for x in new_n:
        new_length.append(len(x))
    print(max(new_length))
