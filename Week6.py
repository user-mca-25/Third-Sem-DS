from array import array

students = {
    1: {
        "Name" : "Farhan",
        "rollNo": 4,
        "marks": 99
    },
    2: {
        "Name" : "Faheem",
        "rollNo": 11,
        "marks": 97
    },
    3: {
            "Name" : "Arsalan",
            "rollNo": 14,
            "marks": 98
        },
        4: {
                    "Name" : "Kaheel",
                    "rollNo": 21,
                    "marks": 97
                },
}

print()
print("Print Dictionary.")
print()

for i in students:
    # print(students[i].values())
    for j in students[i].values():
        print(j, end=" ")
    print()



students[5] = {
    "Name" : "Faizan",
                "rollNo": 17,
                "marks": 97
}

print()
print("Adding Element.")
print()

for i in students:
    # print(students[i].values())
    for j in students[i].values():
        print(j, end=" ")
    print()

students[3]["marks"] = 99

print()
print("Updating.")
print()

for i in students:
    # print(students[i].values())
    for j in students[i].values():
        print(j, end=" ")
    print()

del students[5]

print()
print("Deleting")
print()

for i in students:
    # print(students[i].values())
    for j in students[i].values():
        print(j, end=" ")
    print()

fruits = {
    "apple" : 2,
    "mango" : 8,
    "banana" : 3,
    "grapes" : 4,
}

print()

key = input("Enter any key:- ")

isPresnt = False
for i in fruits.keys():
    if(i == key):
        print("Key is present")
        isPresnt = True
        break    

if(isPresnt == False):
    print("Key not presnt")

print()
print(fruits.items())
print()

fruits_set = {'apple', 'apple', 'mango', 'grapes', 'mango'}

vegetable_set = {'carrot', 'radish', 'tomato','potato', 'onion'}

print(fruits_set.union(vegetable_set));
print(fruits_set.intersection(vegetable_set));
print(fruits_set.difference(vegetable_set));

arr = array("i", [1,2,3,4,5])

def printArray(arr):
    for i in arr:
        print(i, end=" ")

printArray(arr)