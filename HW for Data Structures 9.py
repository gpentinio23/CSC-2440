class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    if root.val==key:
        return root
    if root.val<key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def userInput():
    rootVal = int(input("Enter root value"))
    root = Node(rootVal)
    while True:
        values = int(input("Enter values of tree, 0 when done"))
        if values == 0:
            break
        root = insert(root,values)
    return root

def divisibleByFive(root):
    tot = 0
    if root is None:
        return 0
    if root.val % 5 == 0:
        tot += root.val
    tot+=divisibleByFive(root.left)
    tot+=divisibleByFive(root.right)

    return tot



if __name__ == "__main__":
    tree = (userInput())
    print("Tree using inorder traversal: ")
    inorder(tree)
    print("\nSum of all values divisble by 5")
    sumValues = divisibleByFive(tree)
    print(sumValues)