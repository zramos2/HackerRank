#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
firstElement = 0
lastElement = 0

for i in range(n):
  for j in range(n-1):
    if a[j] > a[j+1]:
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp
      numSwaps = numSwaps + 1

#I have no idea why this doesn't work in hackerrank but it works fine
#print('Array is sorted in %d swaps.' % numSwaps)
#print('Array is sorted in ', numSwaps, ' swaps.')
#print('First Element: ', a[0])
print('Array is sorted in {} swaps.'.format(numSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
