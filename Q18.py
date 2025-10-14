#fibanccoi series
n1=0
n2=1
n=int(input("ENTER THE RANGE:"))
for i in range(0,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n1," ",end="")
