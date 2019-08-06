#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    total = []
    for i in range(4):
        for j in range(4):
            s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum((arr[i+2][j:j+3]))
            total.append(s)
    print(max(total))


# sum() function wont work on this bc append makes it 2d array
# top_arr = []  
# bottom_arr = []

"""
            top_arr.append(arr[i][j:j+3])
            middle_arr = arr[i+1][j+1]
            bottom_arr.append(arr[i+2][j:j+3])
"""
