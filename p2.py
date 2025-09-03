#2.	Write a Program to display all prime numbers within an interval
upperbound=int(input("ENTER THE RANGE :"))
for i in range(2,upperbound+1):
    check=True
    for j in range(2,i):
        if(i%j==0):
            check=False
            break
    if(check):
        print(i)