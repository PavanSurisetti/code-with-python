#prime.py
n=int(input("ENTER THE NUM:"))
for i in range(2,n//2+1):
    if(n%i==0):
        print("NOT PRIME ")
        break
else:
    print("PRIME NUMBER")