print("First there was Hello World")

print("-------------CALCULATOR-------------\n")
a = input("Enter the first number:")
b = input("Enter the second number:")

op = input("Choose the operation(+,-,*,/):")

def sum(a,b):
   print(eval(a+"+"+b))
def sub(a,b):
   print(eval(a+"-"+b))
def mul(a,b):
   print(eval(a+"*"+b))
def div(a,b):
   print(eval(a+"/"+b))

if(op == "+"):
    sum(a,b)
elif(op == "-"):
    sub(a,b)
elif(op == "*"):
    mul(a,b)
elif(op == "/"):
    div(a,b)
else: print("Enter a valid operation")

name = input("Enter your name:")
age = input("Enter your age:")

print("\nName = "+ name, "Age = " + age + "\n")