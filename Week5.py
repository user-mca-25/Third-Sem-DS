#list
list = [1,2,3,4,5,6,7]
count = len(list)
print(count)
print(list)

#Dynamic list

list2 = []
add = True
while(add):
    element = input("Enter Element of list or ; to stop: ")
    if (element == ';'):
        add = False
    else:
        list2.append(int(element))

print(list2)

#max element

max = 0

length = len(list2)
index = 0

for i in range(length):
    if(max < list2[i]):
        max = list2[i]
        index = i
print(list2)
print("Max is", max ,"at index", index)

#reverse

listrev = []

for i in range(length-1,-1,-1):
    listrev.append(list2[i])
    list2.pop()
    


print(listrev)

print(list2)

t = (1,2,2,3,4)
print(type(t))

#t.append(6)
#t.pop
#t.extend([1,3,4])

print(t.count(2))
print(t.index(3))

#insert check
l3 = [1,2,3,4,5]
num = int(input("Enter the number: "))
ind = int(input("Enter index: "))
if (num < l3[ind]):
    l3.insert(ind,num)
print(l3)    

