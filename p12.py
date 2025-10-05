#6.	Write a program to perform any 5 built-in functions by taking any list.
l=[1,2,3]
print(f' before adding elemensts into the list:{l}')
l.insert(0,0)#operation 1
print(f' after adding elemensts into the list:{l}')
print('appending please wait:')
l.append('Shuri')#operaton 2
print(f"after appending:{l}")
l1=[-1,-2,-3,-4,0,1,2,3,4]
print(f"before sorting:{l1}")
l1.sort()#operation 3
print(f"after sorting:{l1}")
l1.pop()#operation 4
print(f"AFTER POPING:{l1}")
l1.clear()#operation 5
print(f"AFTER CLEARING THE DATA IN L1 list:{l1}")
