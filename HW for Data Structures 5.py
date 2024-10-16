from collections import deque#Using deque class to be able to use pop and append functions

#Collects user input to into the array until user enters '0'
def userInput():
    arr = []
    while True:
        value = (int(input("Enter array values or 0 if you're done")))
        if value == 0:
            break
        arr.append(value)
    return arr

#Creates a queue 'q'
#All the input values prior within 'arr' is appended into the queue
#Then the second for loop pops values from the queue and assigns it to the input array
def reverseArray(array):
    q = deque()
    for i in array:
        q.append(i)
    for j in range(len(array)):
#Had to use pop instead of popleft; popleft would maintain the original order of the array, rather than reversing it
        array[j] = q.pop()
    return array

#Print function to remove the brackets and commas
def prints(array):
    for i in range(len(array)):
        print(array[i], end =" ")
    print()

if __name__ == "__main__":
    array = userInput()
    prints(reverseArray(array))
