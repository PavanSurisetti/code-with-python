#6.	Write a program to perform any 5 built-in functions by taking any list.
l=list(eval(input("ENTER THE DATA INTO THE LIST:")))
print(l)
l.append("Bye!")#1appending
print(l)
l.insert(0,'Jai Ganesha')#2inserting
print(l)
l.extend([1,2,3,4,5])#3 exetnding
print(l)
l.remove('Bye!')
print(l)
l.pop()
print(l)
l.clear()
print(l)
