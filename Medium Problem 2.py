class newNode:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
        self.val = data

def insert(root,key):
   if root is None:
       return newNode(key)
   if root.val==key:
       return root
   if root.val<key:
       root.right=insert(root.right,key)
   else:
       root.left=insert(root.left,key)
   return root

def distanceFromRoot(root,x):
    if root.key == x:
        return 0
    elif root.key > x:
        return 1 + distanceFromRoot(root.left,x)
    return 1 + distanceFromRoot(root.right,x)

def distanceBetween2(root,a,b):
    if root == None:
        return 0
    if root.key>a and root.key > b:
        return distanceBetween2(root.left,a,b)
    if root.key<a and root.key < b:
        return distanceBetween2(root.right,a,b)
    if root.key >=a and root.key<=b:
        return (distanceFromRoot(root,a) + distanceFromRoot(root,b))

def findDistWrapper(root,a,b):
    if a > b:
        a, b = b, a
    return distanceBetween2(root,a,b)

def userInput():
#Takes the root node
   rootVal = int(input("Enter root value"))
   root = newNode(rootVal)
   while True:
#Takes all the inputs and inserts them
       values = int(input("Enter values of tree, 0 when done"))
       if values == 0:
           break
       root = insert(root,values)
   return root

if __name__ == "__main__":
    tree = userInput()
    print("Enter what values you want to find the distance between, make sure they are part of the tree")
    input1 = int(input("Enter the value of a: "))
    input2 = int(input("Enter the value of b: "))
    a, b = input1,input2
    print(findDistWrapper(tree,a,b))