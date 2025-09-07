#4.	Demonstrate the following Operators in Python with suitable examples.
#i)	Arithmetic Operators ii) Relational Operators iii) Assignment Operatorsiv) Logical Operators v) Bit wise Operators vi) Ternary Operator vii) Membership Operatorsviii) Identity Operators
print("--ARITHMETIC OPEARTORS--")
a=100
b=30
print(f"add:{a+b}")
print(f"sub:{a-b}")
print(f"mul:{a*b}")
print(f"div:{a/b}")
print(f"mod:{a%b}")
print(f"floor div:{a//b}")
print("--REALATIONAL OPEARTORS--")
print(f"a>b:{a>b}")
print(f"a<b:{a<b}")
print(f"a>=b:{a>=b}")
print(f"a<b:{a<=b}")
print(f"a==b:{a==b}")
print(f"a!=b:{a!=b}")
print("--ASSIGNMENT OPEARTORS--")
v=100
print(f'v:{v}')
print("--LOGICAL OPEARTORS--")
print(f"a and b:{a and b}")
print(f"a or  b:{a or b}")
print(f" not a :{not a}")
print("--BITWISE OPEARTORS--")
print(f"a&b:{a&b}")
print(f"a|b:{a|b}")
print(f"a^b:{a^b}")
print(f"a<<3:{a<<3}")
print(f"b>>4:{b>>4}")
print(f"~a:{~a}")
print("--TERNARY OPEARTORS--")
c=90
big=a if(a>b and a>c) else(b if(b>c) else c)
print(big)
print("--MEMBERSHIP OPERATORS--")
s='hello'
print('z' in s)
print('z'not in s)
print("--IDENTITY  OPERATORS--")
a1=100
b1=100
c1='100'
print(a1 is b1)
print(a1 is c1)
print(a1 is not b1)
print(a1 is not c1)