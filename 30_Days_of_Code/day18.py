import sys

# https://stackabuse.com/stacks-and-queues-in-python/
# Not a good example of stacks and queues

class Solution:
    def __init__(self):
      self.stack = list()
      self.queue = list()
    def pushCharacter(self,s): # add character into the top of the stack  LIFO
      self.stack.append(s)
    def popCharacter(self): # remove character from the top of the stack LIFO
      return self.stack.pop(-1)
    def enqueueCharacter(self,s):   # adds character into the queue  FIFO
      self.queue.append(s)
    def dequeueCharacter(self):   # removes character from queue FIFO
      return self.queue.pop(0)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
