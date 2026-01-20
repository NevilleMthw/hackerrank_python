#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    # For any odd/even, every 3rd day, every leap year etc. we use modulo operator
    # First we ask is it divisible by 2? If the remainder is 0, means even other wise 1 is odd
    # The true test is checking if n (our input) is odd/even first
    if n % 2:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    # Since we have the constraints, we know n > 20, so we just use an else statement
    else:
        print('Not Weird')
