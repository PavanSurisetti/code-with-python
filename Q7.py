#1.	Write a program to define a function with multiple return values.
def data():
    name=input("ENTER THE DATA:")
    age=int(input("ENTER THE AGE:"))
    ph=int(input("ENTER YOUR PHONE NUMBER:"))
    return(name,age,ph)
n,a,p=data()
print(n,a,p)