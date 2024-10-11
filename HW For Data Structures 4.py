from sys import maxsize
def userInput():
    stack = []
    while True:
        value = (int(input("Enter array values or 0 if you're done")))
        if value == 0:
            break
        push(stack,value)
    return stack

def push(stack,item):
    stack.append(item)

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)
    return stack.pop()

def isEmpty(stack):
    return len(stack) == 0

def reverseStack(stack):
    reversedStack = []
    while isEmpty(stack) == False:
        push(reversedStack,stack.pop())
    return reversedStack

def prints(stack):
    for i in range(len(stack)):
        print(stack[i], end = " ")
    print()

if __name__ == "__main__":
    stack = userInput()
    print("Original Stack is:")
    print(stack)
    print("Stack in reverse order is:")
    newStack = reverseStack(stack)
    prints(newStack)