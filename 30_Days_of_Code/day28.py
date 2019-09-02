#!/bin/python3

import math
import os
import random
import re   #this is using regex functions
import sys



if __name__ == '__main__':
    N = int(input())

    lst = []
    for N_itr in range(N):
       firstName, firstNameID = [str(s) for s in input().split()]
       if re.search('@gmail\.com$', firstNameID):
          lst.append(firstName)

    print(*sorted(lst) , sep='\n')
