import math
n=int(input())
s=n**2
l=[]
x=n
while(n>0):
    i=n%10
    l.append(i)
    n=n//10
a=math.pow(10,len(l))
if s%a==x:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
