#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

sys.stdin = StringIO("""10.25
17
5""")

def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost / 100) * tip_percent
    tax = (tax_percent / 100) * meal_cost
    total_value: int = meal_cost + tip + tax
    return round(total_value)

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    result = solve(meal_cost, tip_percent, tax_percent)
    print(result)
