#	Write a program to swap two numbers without using a temporary variable.
n1=2
n2=3
print(f'before swapping :n1->{n1} n2->{n2}')
n1=n1*n2
n2=n1//n2
n1=n1//n2
print(f'after swapping :n1->{n1} n2->{n2}')
