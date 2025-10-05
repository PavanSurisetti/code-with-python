#5.	Write a program to sum all the items in a given dictionary.
d=dict(a=1,b=2,c=3,d=4,e=5)     
sum=0
for i in d.values():
    sum+=i
print(f"sum is :{sum}")