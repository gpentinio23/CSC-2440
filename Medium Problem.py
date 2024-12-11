class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.val = data


def kth_largest(root,k):
    if root is None:
        return -1
    curr = root
    count = 0
    while curr is not None:
        if curr.right is None:
            count+=1
            if count == k:
                return curr.data
            curr = curr.left
        else:
            succ = curr.right
            while succ.left is not None and succ.left != curr:
                succ = succ.left
            if succ.left is None:
                succ.left = curr
                curr = curr.right
            else:
                count +=1
                succ.left = None
                if count == k:
                    return curr.data
                curr = curr.left
    return 1

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

def userInput():
#Takes the root node
   rootVal = int(input("Enter root value"))
   root = Node(rootVal)
   while True:
#Takes all the inputs and inserts them
       values = int(input("Enter values of tree, 0 when done"))
       if values == 0:
           break
       root = insert(root,values)
   return root

def inorder(root):
    if root:
        inorder(root.right)
        print(root.val,end=" ")
        inorder(root.left)

if __name__ == "__main__":
    tree = userInput()
    print("The tree in decreasing order is: ")
    inorder(tree)
    input1 = int(input("\nEnter the k values <= total # of elements"))
    k = input1
    print("\nWith k =" + str(k) + " the K'th largest element is: ")
    print(kth_largest(tree,k))