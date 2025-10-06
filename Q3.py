#3.	Write a program to swap two numbers without using a temporary variable
n1=int(input("ENTER THE NO1:"))
n2=int(input("ENTER THE NO2:"))
print(f"BEFORE SWAP: {n1},{n2}")
n1=n1+n2
n2=n1-n2
n1=n1-n2
print(f"AFTER SWAP: {n1},{n2}")