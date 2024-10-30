d= {"John": "111-222-3333", "Mark": "444-555-6666", "Alex": "999-000-2222"}


def newEntry(name, newNumber):
    d[name] = newNumber
    return d


def searchName(key):
    if key in d:
        print(d[key])
    else:
        print("Name not in phonebook")


def deleteEntry(itemtoDelete):
    del d[itemtoDelete]
    return d


print("Original dictionary: ")
for key, value in d.items():
    print(key, value)

print("\nAfter entering new item: ")
newEntry("Lebron", "111-111-1111")
for key, value in d.items():
    print(key, value)

print("\nSearch for a name: ")
searchName("Mark")
# Test case for name not in dictionary
searchName("Joe")

print("\nAfter deleting an item: ")
deleteEntry("Mark")
for key, value in d.items():
    print(key, value)


