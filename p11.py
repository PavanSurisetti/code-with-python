#5.	Write a program to perform the given operations on a list:
#i.	Addition	 ii. Insertion	 iii. slicing
l=list((10,2.234,'hello',True))
print(f'before adding:{l}')
l1=list((1,2,3,4))
l=l1+l
print(f'after adding:{l}')
print("INSERTION DOING WAIT :")
l.insert(0,'hello alex!')
print(l)
print('SLICING DOING WAIT:')
print(l[1:7])