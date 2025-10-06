#Write a program to find the largest element among three Numbers.
n1=int(input("ENTER THE NO1:"))
n2=int(input("ENTER THE NO2:"))
n3=int(input("ENTER THE NO3:"))
if(n1>n2):
    if(n1>n3):
        print("N1 IS BIG:")
    else:
        print("N3 IS BIG")
else:
    if(n2>n3):
        print("N2 is big")
    else:
        print("N3 IS BIG")