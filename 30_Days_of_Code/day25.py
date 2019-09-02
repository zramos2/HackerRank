# Enter your code here. Read input from STDIN. Print output to STDOUT
# If a number is divisable by another number less or equal to the square root of the first number... it is NOT prime. That is the reason for O(sqrt(n)) run time.


from math import sqrt

prime = True

T = int(input())

for i in range(T):
  n = int(input())

  if n == 1:
    prime = False

  for j in range(2, int(sqrt(n)) + 1):

    if n % j == 0:
      prime = False #Not Prime
      break
    else:
      prime = True #Prime
  if prime:
    print('Prime')
  else:
    print('Not prime')
