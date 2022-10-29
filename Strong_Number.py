import math
a=int(input())
s=0
n=a
while(a>0):
    l=a%10
    x=math.factorial(l)
    s=s+x
    a=a//10
if n==s:print('The number {} is a strong number'.format(n))
else:print('The number {} is not a strong number'.format(n))


    