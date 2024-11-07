
class Node:
    def __init__(self,v):
       self.data=v
       self.left=None
       self.right=None


def insertPreorder(root,key):
    if root is None:
        return Node(key)
    if root.left is None:
        root.left = Node(key)
    else:
        insertPreorder(root.left, key)
    return root


def printPostorder(node):
   if node is None:
       return
   printPostorder(node.left)
   printPostorder(node.right)
   print(node.data,end= " ")


if __name__ == "__main__":
   root = Node(2)
   root.left=Node(3)
   root.right=Node(4)
   root.left.left=Node(5)
   print("Before")
   printPostorder(root)
   print("\nAfter")
   key = 6
   root = insertPreorder(root, key)
   printPostorder(root)

