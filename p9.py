#3.	Write a program to find the length of the string without using any library functions.
string=input("ENTER A STRING:")
count=0
for i in string:
    count+=1
print(f"length is {count}")