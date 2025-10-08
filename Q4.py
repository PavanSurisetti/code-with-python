'''4.	Demonstrate the following Operators in Python with suitable examples.
i)	Arithmetic Operators ii) Relational Operators iii) Assignment Operatorsiv) Logical Operators v) Bit wise Operators vi) Ternary Operator vii) Membership Operatorsviii) Identity Operators
'''
print("-------------ARITHMETIC OPERATORS:--------")
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print("-------------REALTIONAL OPERATORS:--------")
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
print("-------------LOGICAL OPERATORS:--------")
print(a and b)
print(a or b)
print( not b)
print(not a )
print("-------------BITWISE OPERATORS:--------")
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(~a)
print(a<<2)
print(b>>2)
print("-------------SHORT HAND ASSIGNMENT OPERATORS:--------")
a+=10
print(a)
b-=10
print(b)
a*=10
print(a)
b/=10
print(b)
a%=10
print(a)
print("-------------IDENTITY OPERATORS:--------")
print(a is b)
print(a is not b)
print("-------------MEMBERSHIP OPERATORS:--------")
a1='hi'
b1='helo'
print(a1 in b1)
print(a1 not in b1)
print("-------------TERNARY OPERATORS:--------")
big=a if(a>b)  else b
print(big)