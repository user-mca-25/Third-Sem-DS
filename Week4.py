# marks

marks = int (input("Enter Your Marks:"))

if(marks <= 100 and marks > 90):
    print("A+")
elif(marks <= 90 and marks > 80):
    print("B")
elif(marks <= 80 and marks > 60):
    print("C")
else:
    print("Failed")


# even odd

no = 3

if(no % 2 == 0):
    print(no, " is even",)
else:
    print(no, " is odd")

# 10 natural no's

for i in range(1,11):
    print(i, end=" ")

print("")
# factorial 

fact = 5
factorial = 1
for i in range(1, fact+1, 1):
    factorial = factorial * i

print("Factorial of " , fact , " is ", factorial)



# pyramid structure

# for i in range(1,11):
#     for j in range(11-i):
#         print(" ",end="")

#     for k in range(2*i-1):
#         print("*",end="")

#     print("")

#palandrom

number = int(input("Enter the number: "))
rev = 0
ognum = number;
while(number !=0):
    last = number % 10
    number = int(number / 10)
    rev = (rev * 10) + last;

if(rev == ognum):
    print(ognum , "is pallendrome")
else:
    print( ognum , "is not pallendrome")

#pallendrome string
text=[]
text = input("Enter text: ")

length = len(text)
i = 0
flag = True
for j in range(1,int(length/2)):
    if(text[i] != text[-j]):
        print(text,"is not pallendrom")
        flag = False
        break;
    
    i= i+1
if(flag):
    print(text,"is pallendrome")

#fabonacci serires length

a = 0
b = 1
length = int(input("Enter the length: " ))
length = length-2
print(a,b,end=" ")
for i in  range(length):
    c = a + b
    print(c,end=" ")
    a = b 
    b = c

#fabonacci limit
print("")
limit = int(input("Enter the limit: "))
a = 0
b = 1
print(a,b, end=" ")
c = 0
while(c<limit):
    c = a+b
    if(c<=limit):
        print(c, end=" ")
    a = b 
    b = c 






