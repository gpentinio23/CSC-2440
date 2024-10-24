def userInput():
    value1=str(input("Enter first string"))
    value2=str(input("Enter second string"))
    #Checks if inputs are letters and not numbers/special characters
    if value1.isalpha() and value2.isalpha():
        set1 = set(value1)
        set2 = set(value2)
    else:
        print("Invalid Input, Not a string")
    return set1, set2
def uncommonConcat(s1,s2):
    #Checks what letters are not shared between the two sets
    uncommonFirstSet = s1-s2
    uncommonSecondSet = s2-s1
    combined = uncommonFirstSet.union(uncommonSecondSet)
    return combined


if __name__== "__main__":
    s1,s2 = userInput()#So that the sets can be accessed outside the userInput function
    together = (uncommonConcat(s1,s2))
    print(",".join(together))
