#data types 

int = 3
float = 1.5
string = "Hello"

print(type(int) , int)
print(type(float) , float)
print(type(string) , string) 


#string operatios

str1 = "Hello "
str2 = "World"

str3 = str1 + str2
print(str3)

print(str3[:4])

for i_idx, i in enumerate(str3):
    for j_idx, j in enumerate(str3):
    
        if i_idx == j_idx:
            pass
        else:
            if i == j:
                print(i + " repeats")

