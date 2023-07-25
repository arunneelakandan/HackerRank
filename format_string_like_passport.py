#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    formatted_string = ' '.join([i[0].upper() + i[1:] if i else i for i in s.split(' ') ])
    return formatted_string

if __name__ == '__main__':

    s = input()

    print(solve(s))

