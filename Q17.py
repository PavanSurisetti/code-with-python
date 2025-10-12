#5.	Write a program to sum all the items in a given dictionary.
#Q17.py
d=dict(a=1,b=2,c=3,d=4,e=5)
sum=0
for i,j in d.items():
    sum+=j
print(sum)
