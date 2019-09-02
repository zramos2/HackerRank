#!/bin/python3

import math
import os
import random
import re
import sys


#this is using BIT COMPARISON

if __name__ == '__main__':

    T = int(input().strip())
    for _ in range(T):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)



#this is my complicated attempt that doesn't work
'''
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        lst = []

        #setN = set(i for i in range(1,n+1))
        #setK = set(j for j in range(k, n+1))

        setN = list(i for i in range(1,n+1))
        setK = list(j for j in range(k, n+1))

        #print('setN: ', setN)
        #print('setK: ', setK)

        for i in range(len(setN)):
            #if i == 0:
             #   continue
            #lst = []

            for j in range(setN[i],len(setN)):
                #print('n=i => the index: %s  value: %s  ' % (i, setN[i]))
                #print('k=j => the index: %s  value: %s' % (j, setN[j]))
                if setN[i] & setN[j] != 0:

                    bit = setN[i] & setN[j]
                    bit = int(bit)
                    #print('this is bit: ' ,bit)
                    lst.append(bit)
                    #print('this is lst: ', lst)

#https://stackoverflow.com/questions/14793516/how-to-produce-multiple-modes-in-python
        #Counter(lst).most_common() => prints out dictionary of # times it occurs
        #lambda x:x[1] only prints out the '# times it occurs' in the dictionary
        freq = groupby(Counter(lst).most_common(), lambda x:x[1])
        try:
            #print( max( [val for val,count in next(freq)[1]] ) )
            mult_modes = [val for val,count in next(freq)[1]]

            if max(mult_modes) < k:
                print(max(mult_modes))
            else:
                print(mult_modes[-2])

        except StopIteration:
            print(0)

        #print('\n')
'''
