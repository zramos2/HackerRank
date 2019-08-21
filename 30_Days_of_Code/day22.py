class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
#Nice example of BST but NEED TO KNOW MORE!
    def getHeight(self,root):
        if root == None:
          return -1

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if leftHeight > rightHeight:
          return leftHeight + 1
        else:
          return rightHeight + 1


T=int(input())
