#2.	Write a program to count the number of vowels in a string (No control flow allowed).
#Q14.py
str=input("ENTER THE STRING:").lower()
count=0
count+=str.count('a')
count+=str.count('e')
count+=str.count('i')
count+=str.count('o')
count+=str.count('u')
print(f"VOWEL COUNT IN {str}->:{count}")