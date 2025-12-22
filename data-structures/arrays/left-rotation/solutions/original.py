#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

from typing import List

def rotLeft(a: List[int], d: int) -> List[int]:
    # Write your code here
    n = len(a)
    r = d%n 
    return a[r:] + a[:r]
