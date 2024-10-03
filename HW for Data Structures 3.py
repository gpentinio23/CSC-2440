class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
def insertAtEnd(head,new_data):
    new_node = Node(new_data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next=new_node
    return head

def print_list(head):
    curr=head
    while curr is not None:
        print(f"{curr.data}" , end = " ")
        curr=curr.next
    print()

def split(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    if temp is not None:
        temp.prev = None
    return temp

def merge(first,second):
    if first is None:
        return second
    if second is None:
        return first
    if first.data<second.data:
        first.next=merge(first.next,second)
        if first.next is not None:
            first.next.prev = first
        first.prev = None
        return first
    else:
        second.next=merge(first,second.next)
        if second.next is not None:
            second.next.prev=second
        second.prev = None
        return second

def MergeSort(head):
    if head is None or head.next is None:
        return head
    second = split(head)
    head = MergeSort(head)
    second = MergeSort(second)
    return merge(head,second)

def userInputs():
    #Head = None because there are no values yet within the linked list
    head = None
    #Ensures that the user can input as many values as they want
    while True:
        values = (int(input("Enter your values: Type '0' if You're Finished")))
        if values == 0:
            #Breaks ends the while loop
            break
        head = insertAtEnd(head,int(values))
    #Returns the linked list with the user input values
    return head

#Traversing the Linked List to calculate the average
def traverseList(head,total,numofEvenValues):
    while head is not None:
        #Checks if the current value is even or not
        if head.data % 2 == 0:
            numofEvenValues+=1
            total = total + head.data
        head=head.next
    return total/numofEvenValues

if __name__ == "__main__":
    total = 0
    numofEvenValues = 0
    head = userInputs()#Creates the linked list based on the used input
    print("Before Sorting: ")
    print_list(head)
    print("After Sorting: ")
    head=MergeSort(head)#Calls the MergeSort method to sort the linked list in ascending order
    print_list(head)
    print("Average of all even values is: ")#Calculates the average of only the even values
    print(traverseList(head,total,numofEvenValues))

