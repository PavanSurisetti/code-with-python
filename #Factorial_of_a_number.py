#Factorial_of_a_number
num=int(input("Enter a Number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)