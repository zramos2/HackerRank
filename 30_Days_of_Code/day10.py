#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    n = bin(n)[2:].split('0')
  #  print(n)
    n = max(n)
  #  print(n)
    n = len(n)
    print(n)
