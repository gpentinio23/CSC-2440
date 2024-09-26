
def selSort(list):
    for i in range(len(list) - 1):
        #Max index is "reset" to become the next point of comparison in the inner for loop
        maxIndex = i
        #This inner for loops keeps comparing values of the list to one another until new maxValues are found to be swapped
        for j in range(i+1, len(list)):
            if list[maxIndex] < list[j]:
                maxIndex = j
        #Next 3 lines of code are responsible for swapping elements of the list
        temp = list[i]
        list[i] = list[maxIndex]
        list[maxIndex] = temp
    return list
def calcAvgValue(list,total,numOfEvenValues):
    for i in range(len(list)):
        #Modulo operator to check if value is even or not
        if (list[i]) % 2 == 0:
            total += list[i]
            numOfEvenValues += 1
    avg = (total/numOfEvenValues)
    return avg

if __name__ == '__main__':
    list = [2,5,3,1,4,7,6]
    total = 0
    numOfEvenValues = 0
    avg = 0
    #Original List
    print("Before Descending Sort: ")
    for i in range (len(list)):
        print(list[i], end= " ")
    #Sorted List
    print("\nAfter Descending Sort: ")
    selSort(list)
    for i in range(len(list)):
        print(list[i], end = " ")
    #Average of even numbers
    print("\nThe Average value of all even numbers in the list is: " + str((int(calcAvgValue(list,total,numOfEvenValues)))))