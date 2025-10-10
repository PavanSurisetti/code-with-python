#4.	Write a program to check if the substring is present in a given string or not.
str=input("ENTER THE STRING:")
keystr=input("ENTER SUB STRING TO SEARCH IN THE STRING:")
if(keystr in str):
    print("THE SUBSTRING THERE!")
else:
    print("NOPE!")