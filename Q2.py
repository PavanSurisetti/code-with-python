#2.	Write a Program to display all prime numbers within an interval
interval=int(input("ENTER THE RANGE YOU WANT:"))
for i in range(2,interval):
    for j in range(2,i//2+1):
        if(i%j==0):
            break
    else:
        print(i)