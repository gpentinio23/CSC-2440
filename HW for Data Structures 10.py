class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.val=data

#Added new parameter count to keep track of visited nodes
def calculateSum(root, k, ans,count):
    if root is None or count[0] >=k:
        return
    #Sums all the elements >= 0 for the right side of three
    if root.right is not None:
        calculateSum(root.right, k, ans,count)
    #The tracker comparing how many nodes we've visited
    if count[0] < k:
        count[0]+=1
        ans[0]+=root.data
    # Sums all the elements >= 0 for the left side of three
    if root.left is not None:
        calculateSum(root.left, k, ans,count)
    else:
        return


def sum_k_largest(root, k):
    ans = [0]
    count= [0]
    calculateSum(root, k, ans, count)
    return ans[0]

#Function to insert the user inputs into the tree using inorder traversal
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
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

if __name__ == "__main__":
    tree = userInput()
    print("The values of the tree are: ")
    inorder(tree)
    print()
    k = 3
    print("With k = 3, the largest element is 9 so the sum of all elements greater than or equal to 9 is: ")
    print(sum_k_largest(tree, k))
