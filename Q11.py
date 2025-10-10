'''5.	Write a program to perform the given operations on a list:
i.	Addition	 ii. Insertion	 iii. slicing
'''
l=list(eval(input("ENTER THE ELEMENTS INTO THE LIST1:")))
print(l)
l1=list(eval(input("ENTER THE ELEMENTS INTO THE LIST2:")))
print(l1)
l2=l+l1
print(l2)#addition
l.insert(0,'JAI GANESHA')#insertion
print(l)
print(l2[:4])#slicing
