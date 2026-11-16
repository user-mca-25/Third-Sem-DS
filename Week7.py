import numpy as np

"""
arr = np.array([[1,2,3,],
                [4,5,6],
                [7,8,9]])

print("diagonal")

for i in range(3):
    for j in range(3):
        if i == j:
            print(arr[i,j])

print("rev diagonal")

for i in range(3):
    for j in range(3):
        if i+j == len(arr[0])-1:
            print(arr[i,j])


print(arr)

print(arr * 2)
print(arr[2,2])

print("methods")

print(arr.size)
print(arr.shape)
print(arr.ndim)
"""
print("array slicing")

arr1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print()
print("row")
print(arr1[:1:1,::])
print()
print("column")
print(arr1[::,2::])
print()
print("reverse")
print(arr1[::-1,::-1])
print()
print("arithmatic operations on numpy arrays")

arr2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print()
print("addition")

print(arr1 + arr2)
print()
print("substraction")

print(arr2-arr1)
print()
print("multiplication")

print(arr2*arr1)
print()
print("division")

print(arr2/arr1)
print()
print("null matrix")

print(np.zeros((3,3)))
print()
print("identity matrix")

print(np.eye(3,3))
print()
print("a range")

print(np.arange(0,9,1))
print()
print("line space")

print(np.linspace(0,25,6))

print()
print("rehape")

print(np.arange(0,10,1).reshape(2,5))