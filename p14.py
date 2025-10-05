#2.	Write a program to count the number of vowels in a string (No control flow allowed).
s=input('enter a string:').lower()
count=0
count+=s.count('a')
count+=s.count('e')
count+=s.count('i')
count+=s.count('o')
count+=s.count('u')
print(f"vowels in {s} is {count}")