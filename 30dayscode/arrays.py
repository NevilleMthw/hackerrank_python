#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""1
    1 2 3 4
    """)
if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    arr.reverse()
    
    # The map() is used to take str, tuples or lists as input and then return as the map obeject which
    # is one of the iterables (str, list or tuple)
    print(type(' '.join(map(str, arr))))

        
